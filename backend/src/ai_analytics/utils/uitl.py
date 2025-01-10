#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：uitl.py
@Author  ：yohong
@Date    ：2025/1/10 18:04 
"""

import contextlib
import os
from os import PathLike
from typing import Union


@contextlib.contextmanager
def chdir(path: Union[str, PathLike]):
	cwd = os.getcwd()
	os.chdir(path)
	yield
	os.chdir(cwd)
