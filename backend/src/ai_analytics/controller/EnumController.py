#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigController.py
@Author  ：yohong
@Date    ：2025/1/10 15:05 
"""
import sys

from fastapi import APIRouter, Depends

import inspect

from ai_analytics.common.enums import BaseEnum

from ai_analytics.controller import ResponseModel

router = APIRouter()


@router.get('/enum/name={enum_name}', response_model=ResponseModel)
def enum(enum_name: str):
	current_module = sys.modules[__name__]
	data = None
	for name, obj in inspect.getmembers(current_module, inspect.isclass):
		if issubclass(obj, BaseEnum) and obj.__name__ == enum_name:
			data = obj.list_all()
	return ResponseModel(code=200, msg="Success", data=data)
