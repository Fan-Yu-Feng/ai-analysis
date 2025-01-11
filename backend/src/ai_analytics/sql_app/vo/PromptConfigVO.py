#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：PromptConfigVO.py
@Author  ：yohong
@Date    ：2025/1/10 14:29 
"""
from pydantic import BaseModel


class BasePromptConfig(BaseModel):
	pass


class PromptConfigCreateSchema(BasePromptConfig):
	"""
	请求模型验证：
	pass
	"""
	pass


class PromptConfigUpdateSchema(BasePromptConfig):
	"""
	请求模型验证：
	"""
	pass

class PromptConfigSchema(BasePromptConfig):
	"""
	响应模型验证：
	"""
	pass