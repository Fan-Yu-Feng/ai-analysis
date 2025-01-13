#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：__init__.py.py
@Author  ：yohong
@Date    ：2025/1/10 15:35 
"""

from pydantic import BaseModel
from typing import Any, Optional

class ResponseModel(BaseModel):
    code: int
    msg: str
    data: Optional[Any] = None