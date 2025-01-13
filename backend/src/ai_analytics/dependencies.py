#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：dependencies.py
@Author  ：yohong
@Date    ：2025/1/10 15:04 
"""

from fastapi import Request
from sqlalchemy.orm import Session

from ai_analytics.sql_app.config.database import SessionLocal


#
# def get_db(request: Request) -> Session:
#     return request.state.db


def get_db():
	"""
	每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
	:return:
	"""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


class CommonQueryParams:
	def __init__(self, page_no: int = 1, page_size: int = 10):
		self.page_no = page_no
		if self.page_no < 1:
			self.page_no = 1
		self.page_size = page_size

		if self.page_size < 0:
			self.page_size = 10
