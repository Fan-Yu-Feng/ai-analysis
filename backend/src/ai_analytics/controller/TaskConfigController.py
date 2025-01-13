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


@router.get('/task-config/page')
def get_by_page(
		session: Session = Depends(get_db),
		commons: CommonQueryParams = Depends()
):
	return _service.get_by_page(page_no=commons.page_no, page_size=commons.page_size)


@router.get('/task-config/get-by-id/{pk}')
def get_by_id(
		pk: int,
		session: Session = Depends(get_db)
):
	logger.info(f'pk: {pk}')
	return _service.get_by_id(pk)


@router.post('/task-config/add', response_model=TaskConfigSchema)
def create(
		obj_in: TaskConfigCreateSchema,
		session: Session = Depends(get_db),
):
	return _service.create(obj_in)


@router.post('/task-config/update', response_model=TaskConfigSchema)
def patch(
		obj_in: TaskConfigUpdateSchema,
		session: Session = Depends(get_db)
):
	return _service.update(obj_in)


@router.delete('/task-config/delete/{pk}')
def delete(
		pk: int,
		session: Session = Depends(get_db)
):
	return _service.delete(pk)
