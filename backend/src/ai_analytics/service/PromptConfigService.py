#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：PromptConfigService.py
@Author  ：yohong
@Date    ：2025/1/10 15:07 
"""
from ai_analytics.service.BaseService import BaseService
from ai_analytics.sql_app.dao.PromptConfigDAO import PromptConfigDAO
from ai_analytics.sql_app.dataobject import PromptConfigDO
from ai_analytics.sql_app.vo.PromptConfigVO import PromptConfigCreateSchema, PromptConfigUpdateSchema


class PromptConfigService(BaseService[PromptConfigDO, PromptConfigCreateSchema, PromptConfigUpdateSchema]):
    dao = PromptConfigDAO()