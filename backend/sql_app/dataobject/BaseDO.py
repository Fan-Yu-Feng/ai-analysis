#!/usr/bin/env python

import time
from uuid import uuid4
from sqlalchemy import String, Integer, BigInteger
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    __table_args__ = {
        'mysql_charset': 'utf8mb4'
    }

    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def columnitems(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    @property
    def dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.columnitems)

    def tojson(self):
        return self.columnitems


class BaseObj(Base):
    # 公共字段
    id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')
    create_time = Column(Integer, default=lambda: int(time.time()), nullable=False)
    update_time = Column(Integer, default=lambda: int(time.time()), nullable=False, onupdate=lambda: int(time.time()))
    deleted = Column(Integer, default=0)
    create_by = Column(String(255), nullable=True, comment='创建者')
    update_by = Column(String(255), nullable=True, comment='修改者')
    pass


BaseDO = declarative_base(cls=BaseObj)