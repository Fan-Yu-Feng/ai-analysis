#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigService.py
@Author  ：yohong
@Date    ：2025/1/10 15:07 
"""
from ai_analytics.common.enums import TaskTypeEnum
from ai_analytics.service.BaseService import BaseService
from ai_analytics.service.TaskFactory import TaskFactory
from ai_analytics.sql_app.dao.TaskConfigDAO import TaskConfigDAO
from ai_analytics.sql_app.dataobject import TaskConfigDO
from ai_analytics.sql_app.vo.TaskConfigVO import TaskConfigCreateSchema, TaskConfigUpdateSchema


class TaskConfigService(BaseService[TaskConfigDO, TaskConfigCreateSchema, TaskConfigUpdateSchema]):
	dao = TaskConfigDAO()

	async def start_task(self, session, pk):
		"""Start a task"""
		config_do = self.dao.get_by_id(session, pk)
		if config_do is None:
			raise Exception('Task not found')
		taskTypeEnum = TaskTypeEnum.get_by_code(config_do.task_type)
		task = TaskFactory.get_task(taskTypeEnum)
		if task is None:
			raise Exception('Unknown task type')

		task._process_task(config_do)
		return True
