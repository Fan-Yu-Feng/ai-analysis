#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigService.py
@Author  ：yohong
@Date    ：2025/1/10 15:07 
"""
from ai_analytics.service.BaseService import BaseService
from ai_analytics.sql_app.dao.TaskConfigDAO import TaskConfigDAO
from ai_analytics.sql_app.dataobject import TaskConfigDO
from ai_analytics.sql_app.vo.TaskConfigVO import TaskConfigCreateSchema, TaskConfigUpdateSchema


class TaskConfigService(BaseService[TaskConfigDO, TaskConfigCreateSchema, TaskConfigUpdateSchema]):
    dao = TaskConfigDAO
