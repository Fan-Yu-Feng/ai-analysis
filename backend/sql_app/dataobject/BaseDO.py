#!/usr/bin/env python

import time
from sqlalchemy import String, Integer, BigInteger
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
	__table_args__ = {
		'mysql_charset': 'utf8mb4'
	}

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
	# 公共字段
	id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')
	create_time = Column(Integer, default=lambda: int(time.time()), nullable=False)
	update_time = Column(Integer, default=lambda: int(time.time()), nullable=False, onupdate=lambda: int(time.time()))
	deleted = Column(Integer, default=0, nullable=False, comment='是否删除，0未删除，1已删除')
	create_by = Column(String(255), nullable=True, default='sys', comment='创建者')
	update_by = Column(String(255), nullable=True, default='sys', comment='修改者')
	pass


BaseDO = declarative_base(cls=BaseObj)
