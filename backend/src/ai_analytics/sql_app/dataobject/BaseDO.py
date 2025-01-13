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

