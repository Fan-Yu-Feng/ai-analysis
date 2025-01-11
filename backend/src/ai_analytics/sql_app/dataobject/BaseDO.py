#!/usr/bin/env python

import time
from datetime import datetime

from sqlalchemy import String, Integer, BigInteger, DateTime
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr


class Base(object):
	__table_args__ = {
		'mysql_engine': 'InnoDB',
		'mysql_collate': 'utf8mb4_general_ci'
	}

	def __init__(self):
		self.__table__ = None

	@property
	def columns(self):
		"""
		返回所有字段名
		:return:
		"""
		return [c.name for c in self.__table__.columns]

	@property
	def columnitems(self):
		"""
		返回字典格式数据
		:return:  dict
		"""
		return dict([(c, getattr(self, c)) for c in self.columns])

	@property
	def dict(self):
		return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

	def __repr__(self):
		return '{}({})'.format(self.__class__.__name__, self.columnitems)

	def tojson(self):
		"""
		返回json格式数据
		:return:
		"""
		return self.columnitems


class BaseObj(Base):
	@declared_attr
	def __tablename__(cls):
		return cls.__name__.lower()

	# 公共字段
	id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')
	create_time = Column(DateTime, default=datetime.utcnow, nullable=False, comment='创建时间')
	update_time = Column(DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.utcnow, comment='更新时间')
	deleted = Column(Integer, default=0, nullable=False, comment='是否删除，0未删除，1已删除')
	create_by = Column(String(255), nullable=True, default='sys', comment='创建者')
	update_by = Column(String(255), nullable=True, default='sys', comment='修改者')
	pass


BaseDO = declarative_base(cls=BaseObj)

# backend/sql_app/dataobject/PromptConfigDO.py
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Boolean


class PromptConfigDO(BaseDO):
	__tablename__ = 'prompt_config'

	sentiment = Column(String(255), nullable=False, comment='情感倾向：正面、负面、中性')
	topic = Column(String(255), comment='主要主题')
	summary = Column(String(255), nullable=False, comment='总结类：对产品的看法、对营销手段的评论、表达向往、表达讽刺、其他')
	ext_info = Column(Text, comment='扩展字段，存储其他的 prompt')
	system_prompt = Column(Text, comment='系统 prompt')
	user_prompt = Column(Text, comment='用户 prompt')
	deleted = Column(Boolean, nullable=False, default=False, comment='逻辑删除标志，0 表示未删除，1 表示已删除')
	create_by = Column(String(255), nullable=False, comment='创建人')
	update_by = Column(String(255), nullable=False, comment='修改人')
	create_time = Column(DateTime, default=lambda: datetime.utcnow(), comment='创建时间')
	update_time = Column(DateTime, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow(),
	                     comment='更新时间')
