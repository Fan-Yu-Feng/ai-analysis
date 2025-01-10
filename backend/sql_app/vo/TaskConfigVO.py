#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigVO.py
@Author  ：yohong
@Date    ：2025/1/10 14:29 
"""
from pydantic import BaseModel


class BaseTaskConfig(BaseModel):
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
	pass
