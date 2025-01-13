#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigVO.py
@Author  ：yohong
@Date    ：2025/1/10 14:29 
"""

from ai_analytics.sql_app.vo.schemas import BaseRespVO


class BaseTaskConfig(BaseRespVO):
	# id: int
	prompt_config_id: int
	status: str
	task_type: str
	priority: int
	config_detail: str
	error_message: str


class TaskConfigCreateSchema(BaseTaskConfig):
	"""
	请求模型验证：
	pass
	"""
	pass


class TaskConfigUpdateSchema(BaseTaskConfig):
	"""
	请求模型验证：
	"""
	id: int


class TaskConfigSchema(BaseTaskConfig):
	"""
	响应模型验证：
	"""
	pass
