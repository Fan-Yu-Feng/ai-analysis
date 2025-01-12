#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigController.py
@Author  ：yohong
@Date    ：2025/1/10 15:05 
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ai_analytics.common.log import logger

from ai_analytics.dependencies import CommonQueryParams, get_db
from ai_analytics.sql_app.vo.TaskConfigVO import (TaskConfigSchema, TaskConfigCreateSchema,
                                                  TaskConfigUpdateSchema)
from ai_analytics.service.TaskConfigService import TaskConfigService

router = APIRouter()

_service = TaskConfigService()


@router.get('/task-config')
def get(
		session: Session = Depends(get_db),
		commons: CommonQueryParams = Depends()
):
	return _service.get_by_page(page=commons.page, page_size=commons.page_size)


@router.get('/task-config/{pk}')
def get_by_id(
		pk: int,
		session: Session = Depends(get_db)
):
	logger.info(f'pk: {pk}')
	return _service.get_by_id(pk)


@router.post('/task-config', response_model=TaskConfigSchema)
def create(
		obj_in: TaskConfigCreateSchema,
		session: Session = Depends(get_db),
):
	return _service.create(obj_in)


@router.patch('/task-config/{pk}', response_model=TaskConfigSchema)
def patch(
		pk: int,
		obj_in: TaskConfigUpdateSchema,
		session: Session = Depends(get_db)
):
	return _service.patch(obj_in)


@router.delete('/task-config/{pk}')
def delete(
		pk: int,
		session: Session = Depends(get_db)
):
	return _service.delete(pk)
