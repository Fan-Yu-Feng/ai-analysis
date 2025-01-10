#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：BaseService.py
@Author  ：yohong
@Date    ：2025/1/10 13:58 
"""
from typing import Generic, List

from backend.src.sql_app.dao.BaseDAO import BaseDAO
from backend.src.sql_app.vo.schemas import ModelType, CreateSchema, UpdateSchema


class BaseService(Generic[ModelType, CreateSchema, UpdateSchema]):
	dao: BaseDAO

	def get_by_page(self, page=1, page_size=10) -> List[ModelType]:
		""""""
		return self.dao.get_page_by_start_id(page, page_size)

	def total(self, id) -> int:
		return self.dao.count()

	def get_by_id(self, id, pk: int) -> ModelType:
		"""Get by id"""
		return self.dao.get_by_id(pk)

	def create(self, id, obj_in: CreateSchema) -> ModelType:
		"""Create a object"""
		return self.dao.add(obj_in)

	def patch(self, obj_in: UpdateSchema) -> ModelType:
		"""Update"""
		return self.dao.update_by_id(obj_in)

	def delete(self, pk: int) -> int:
		"""Delete a object"""
		return self.dao.delete_by_id(pk)
