#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskFactory.py
@Author  ：yohong
@Date    ：2025/1/10 11:40 
"""

# task_factory.py
from backend.service.CommentAnalysisTask import CommentAnalysisTask
from backend.common.enums import TaskTypeEnum


class TaskFactory:
	"""
	任务工厂类
	"""
	_instances = {}

	@staticmethod
	def get_task(task_type: TaskTypeEnum):
		"""
		获取任务实例
		:param task_type:
		:return:
		"""
		if task_type not in TaskFactory._instances:
			if task_type == TaskTypeEnum.AnalysisComment:
				TaskFactory._instances[task_type] = CommentAnalysisTask()
		# Add other task types here
		# elif task_type == TaskTypeEnum.OtherTaskType:
		#     TaskFactory._instances[task_type] = OtherTaskClass()
		return TaskFactory._instances[task_type]
