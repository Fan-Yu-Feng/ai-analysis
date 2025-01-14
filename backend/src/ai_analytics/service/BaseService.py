#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：BaseService.py
@Author  ：yohong
@Date    ：2025/1/10 13:58 
"""
from typing import Generic, List

from sqlalchemy.orm import Session

from ai_analytics.sql_app.dao.BaseDAO import BaseDAO
from ai_analytics.sql_app.vo.schemas import ModelType, CreateSchema, UpdateSchema
from ai_analytics.common.log import logger


class BaseService(Generic[ModelType, CreateSchema, UpdateSchema]):
	dao: BaseDAO

	def get_by_page(self, session: Session = None, page_no=1, page_size=10, ) -> List[ModelType]:
		""""""
		# TODO 分页接口还没写，后面在补充，list && total
		return self.dao.get_page_by_start_id(session,page_no, page_size)

	def total(self, session: Session, reqVo: CreateSchema) -> int:
		return self.dao.count(session)

	def get_by_id(self, session: Session,pk: int) -> ModelType:
		"""Get by id"""
		logger.info(f'pk: {pk}')
		return self.dao.get_by_id(session,pk)

	def create(self, session: Session, obj_in: CreateSchema) -> ModelType:
		"""Create a object"""
		return self.dao.add(session,obj_in)

	def update(self, session: Session,obj_in: UpdateSchema) -> ModelType:
		"""Update"""
		return self.dao.update_by_id(session,obj_in)

	def delete(self,session: Session, pk: int) -> int:
		"""Delete a object"""
		return self.dao.delete_by_id(session,pk)
