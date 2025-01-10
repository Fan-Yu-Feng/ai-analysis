#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigService.py
@Author  ：yohong
@Date    ：2025/1/10 15:07 
"""
from backend.src.service.BaseService import BaseService
from backend.src.sql_app.dataobject import TaskConfigDO
from backend.src.sql_app.vo.TaskConfigVO import TaskConfigCreateSchema, TaskConfigUpdateSchema


class TaskConfigService(BaseService[TaskConfigDO, TaskConfigCreateSchema, TaskConfigUpdateSchema]):
    dao = TaskConfigDO()
