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

from backend.dependencies import CommonQueryParams, get_db
from backend.src.sql_app.vo.TaskConfigVO import (TaskConfigSchema, TaskConfigCreateSchema,
                                                 TaskConfigUpdateSchema)
from backend.src.service import TaskConfigService

router = APIRouter()

_service = TaskConfigService()


@router.get('/task-config')
def get(
		session: Session = Depends(get_db),
		commons: CommonQueryParams = Depends()
):
	return _service.get(session, offset=commons.offset, limit=commons.limit)


@router.get('/task-config/{pk}')
def get_by_id(
		pk: int,
		session: Session = Depends(get_db)
):
	return _service.get_by_id(session, pk)


@router.post('/task-config', response_model=TaskConfigSchema)
def create(
		obj_in: TaskConfigCreateSchema,
		session: Session = Depends(get_db),
):
	return _service.create(session, obj_in)


@router.patch('/task-config/{pk}', response_model=TaskConfigSchema)
def patch(
		pk: int,
		obj_in: TaskConfigUpdateSchema,
		session: Session = Depends(get_db)
):
	return _service.patch(session, pk, obj_in)


@router.delete('/task-config/{pk}')
def delete(
		pk: int,
		session: Session = Depends(get_db)
):
	return _service.delete(session, pk)
