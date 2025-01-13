#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：BaseService.py
@Author  ：yohong
@Date    ：2025/1/10 13:58 
"""
from typing import Generic, List

from ai_analytics.sql_app.dao.BaseDAO import BaseDAO
from ai_analytics.sql_app.vo.schemas import ModelType, CreateSchema, UpdateSchema
from ai_analytics.common.log import logger

class BaseService(Generic[ModelType, CreateSchema, UpdateSchema]):
	dao: BaseDAO

	def get_by_page(self, page_no=1, page_size=10) -> List[ModelType]:
		""""""
		return self.dao.get_page_by_start_id(page_no, page_size)

	def total(self, reqVo:CreateSchema) -> int:
		return self.dao.count()

	def get_by_id(self, pk: int) -> ModelType:
		"""Get by id"""
		logger.info(f'pk: {pk}')
		return self.dao.get_by_id(pk)

	def create(self, obj_in: CreateSchema) -> ModelType:
		"""Create a object"""
		return self.dao.add(obj_in)

	def update(self, obj_in: UpdateSchema) -> ModelType:
		"""Update"""
		return self.dao.update_by_id(obj_in)

	def delete(self, pk: int) -> int:
		"""Delete a object"""
		return self.dao.delete_by_id(pk)
