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


def get_db(request: Request) -> Session:
    return request.state.db


class CommonQueryParams:
    def __init__(self, offset: int = 1, limit: int = 10):
        self.offset = offset - 1
        if self.offset < 0:
            self.offset = 0
        self.limit = limit

        if self.limit < 0:
            self.limit = 10