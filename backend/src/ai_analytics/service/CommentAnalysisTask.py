#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Desc    : 评论分析任务类
@File    ：CommentAnalysisTask.py
@Author  ：yohong
@Date    ：2025/1/9 17:02
"""
import asyncio

from ai_analytics.common.enums import TaskStatusEnum, TaskTypeEnum
from ai_analytics.core.agents.comment_analysis import GeneralAnalysisInfoExtractor
from ai_analytics.service.BaseTask import BaseTask
from ai_analytics.sql_app.dao.CommentAnalyticsInfoDAO import CommentAnalyticsInfoDAO
from ai_analytics.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO
from ai_analytics.sql_app.dataobject import TaskConfigDO
from ai_analytics.sql_app.vo.CommentAnalyticsInfoVO import CommentAnalyticsInfoCreate
from ai_analytics.common.log import logger


class CommentAnalysisTask(BaseTask):

	def __init__(self, max_workers=5):
		super().__init__(max_workers)

	def _get_wait_tasks(self) -> list[TaskConfigDO]:
		"""
		获取待处理任务
		"""
		# Fetch tasks from the source and add to the queue
		# Example: self.task_queue.put((priority, task))
		return self._task_config_dao.get_by_filters_do(
			TaskConfigDO(status=TaskStatusEnum.WAIT, task_type=self.get_task_type()))

	def get_task_type(self) -> TaskTypeEnum:
		return TaskTypeEnum.AnalysisComment

	def _fetch_tasks(self):
		"""
		定时拉取任务，这个方法是私有的
		"""
		# Fetch tasks from the source and add to the queue
		# Example: self.task_queue.put((priority, task))
		# 拉取待处理的任务
		wait_task_list = self._get_wait_tasks()
		for task in wait_task_list:
			# 更新任务为处理中
			count = self.update_task_status(task.id, TaskStatusEnum.WAIT, TaskStatusEnum.PROGRESS)
			if count == 0:
				# 说明任务已经被其他线程处理了
				continue
			self.push_task(task.priority, task)
		pass

	def _process_task(self, task: TaskConfigDO):
		"""
		process task
		:param task: task object
		"""
		# Implement the actual task PROGRESS logic here
		try:

			asyncio.run(self.run(task))
			# 更新任务状态为已完成
			self.update_task_status(task.id, TaskStatusEnum.PROGRESS, TaskStatusEnum.SUCCESS)
		except Exception as e:
			logger.error(f"Error PROGRESS task {task.id}: {e}")
			# 更新任务状态为失败
			self.update_task_status(task.id, TaskStatusEnum.PROGRESS, TaskStatusEnum.FAILED, str(e))

	async def run(self, task: TaskConfigDO):
		# Run the comment analysis task
		# 获取任务的 prompt
		prompt_do = self._prompt_config_dao.get_by_id(task.prompt_config_id)
		# 获取评论数据
		socialCommentListDao = SocialMediaCommentListDAO.getInstance()
		startId = 1822240937
		social_comment_list = socialCommentListDao.get_page_by_start_id(1, 20, startId)
		gie = GeneralAnalysisInfoExtractor(prompt_do.system_prompt, prompt_do.user_prompt)
		while len(social_comment_list) > 0:
			startId = social_comment_list[-1].id
			# 组装数据。格式是[{id: comment.id, content: comment.comment_content_}]
			assembled_data = [{'id': comment.id, 'content': comment.comment_content} for comment in
			                  social_comment_list]
			logger.info(assembled_data)

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
					logger.info(f"Error PROGRESS comment_id {comment_id}: {e}")
			comment_analytics_info = CommentAnalyticsInfoDAO.getInstance()
			comment_analytics_info.add_all(comment_analytics_info_list)

			social_comment_list = socialCommentListDao.get_page_by_start_id(1, 10, startId)


# Insert the data into the database
if __name__ == '__main__':
	task = CommentAnalysisTask()
	task.start_fetching()

	asyncio.run(task.run())
