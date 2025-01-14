#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigVO.py
@Author  ：yohong
@Date    ：2025/1/10 14:29 
"""
from typing import Optional

from ai_analytics.sql_app.vo.schemas import BaseRespVO


class BaseTaskConfig(BaseRespVO):
	# id: int
	# prompt_config_id: Optional[int]
	# status: str
	# task_type: Optional[str]
	# priority: Optional[int]
	# config_detail: Optional[str]
	# error_message: Optional[str]
	pass

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
	status: str


class TaskConfigSchema(BaseTaskConfig):
	"""
	响应模型验证：
	"""
	pass
