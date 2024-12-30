import asyncio
import json
import os

from backend.core.agents.comment_analysis import GeneralAnalysisInfoExtractor
from backend.core.utils.general_utils import get_logger
from backend.sql_app.dao.CommentAnalyticsInfoDAO import CommentAnalyticsInfoDAO
from backend.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO
from backend.sql_app.vo.CommentAnalyticsInfoVO import CommentAnalyticsInfoCreate


class CommentAnalysisTask():
	def __init__(self):
		pass
		# self.comment = comment



	def get_comment_list(self):
		# Get the list of comments

		return self.comment_list


	async def run(self):
		# Run the comment analysis task
		# 获取评论数据
		socialCommentListDao = SocialMediaCommentListDAO.getInstance()
		social_comment_list = socialCommentListDao.get_paginated_comments(1, 5)
		# 组装评论数据
		# 组装数据。格式是[{id: comment.id_, content: comment.comment_content_}]
		assembled_data = [{'id': comment.id_, 'content': comment.comment_content_} for comment in social_comment_list]

		print(assembled_data)
		project_dir = os.environ.get("PROJECT_DIR", "/Users/yohong/code/yohong/wiseflow")
		wiseflow_logger = get_logger('general_process', project_dir)
		gie = GeneralAnalysisInfoExtractor(wiseflow_logger)
		# comment_list = json.loads(comment)

		# 每 10 个 comment 拼接为 str 然后调用一次接口

		data_dict = await gie.get_anlalysis_res(assembled_data)

		# 调用接口获取评论分析结果
		print(data_dict)
		# 解析数据
		comment_analytics_info_list = [
			CommentAnalyticsInfoCreate(
				comment_id=int(comment_id),
				content=info['comment'],
				sentiment=info['sentiment'],
				topic=info.get('topic'),
				keywords=info.get('keywords'),
				summary=info['summary']
			)
			for comment_id, info in data_dict.items()
		]
		comment_analytics_info = CommentAnalyticsInfoDAO.getInstance()
		comment_analytics_info.add_all(comment_analytics_info_list)
		# 保存评论分析结果
		return social_comment_list

# Insert the data into the database
if __name__ == '__main__':
	comment = CommentAnalysisTask()
	asyncio.run(comment.run())
