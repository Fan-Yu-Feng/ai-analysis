import asyncio

from backend.core.agents.comment_analysis import GeneralAnalysisInfoExtractor
from backend.sql_app.dao.CommentAnalyticsInfoDAO import CommentAnalyticsInfoDAO
from backend.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO
from backend.sql_app.vo.CommentAnalyticsInfoVO import CommentAnalyticsInfoCreate
from common.log import logger


class CommentAnalysisTask():
	def __init__(self):
		pass

	def get_comment_list(self):
		return self.comment_list

	async def run(self):
		# Run the comment analysis task
		# 获取评论数据
		socialCommentListDao = SocialMediaCommentListDAO.getInstance()
		startId = 1822240937
		social_comment_list = socialCommentListDao.get_page_by_start_id(1, 20, startId)
		while len(social_comment_list) > 0:
			startId = social_comment_list[-1].id_
			# 组装数据。格式是[{id: comment.id_, content: comment.comment_content_}]
			assembled_data = [{'id': comment.id_, 'content': comment.comment_content_} for comment in
			                  social_comment_list]

			logger.info(assembled_data)

			gie = GeneralAnalysisInfoExtractor()
			# comment_list = json.loads(comment)

			# 每 10 个 comment 拼接为 str 然后调用一次接口
			data_dict = await gie.get_anlalysis_res(assembled_data)

			# 调用接口获取评论分析结果
			logger.info(data_dict)
			# 解析数据
			comment_analytics_info_list = []
			for comment_id, info in data_dict.items():
				try:
					comment_analytics_info = CommentAnalyticsInfoCreate(
						comment_id=int(comment_id),
						content=info['comment'],
						sentiment=info['sentiment'],
						topic=info.get('topic'),
						keywords=info['keywords'] if isinstance(info['keywords'], list) else [info['keywords']],
						summary=info['summary']
					)
					comment_analytics_info_list.append(comment_analytics_info)
				except Exception as e:
					logger.info(f"Error processing comment_id {comment_id}: {e}")
			comment_analytics_info = CommentAnalyticsInfoDAO.getInstance()
			comment_analytics_info.add_all(comment_analytics_info_list)

			social_comment_list = socialCommentListDao.get_page_by_start_id(1, 10, startId)


# Insert the data into the database
if __name__ == '__main__':
	comment = CommentAnalysisTask()
	asyncio.run(comment.run())
