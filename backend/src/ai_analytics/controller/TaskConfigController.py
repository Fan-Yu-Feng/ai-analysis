#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskConfigController.py
@Author  ：yohong
@Date    ：2025/1/10 15:05 
"""
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ai_analytics.common.log import logger
from ai_analytics.controller import ResponseModel
from ai_analytics.dependencies import CommonQueryParams, get_db
from ai_analytics.sql_app.vo.TaskConfigVO import (TaskConfigSchema, TaskConfigCreateSchema, TaskConfigUpdateSchema)
from ai_analytics.service.TaskConfigService import TaskConfigService

router = APIRouter()
_service = TaskConfigService()


@router.get('/task-config/page', response_model=ResponseModel)
def get_by_page(session: Session = Depends(get_db), commons: CommonQueryParams = Depends()):
	data = _service.get_by_page(page_no=commons.page_no, page_size=commons.page_size, session=session)
	return ResponseModel(code=200, msg="Success", data=[i.dict for i in data])


@router.get('/task-config/get-by-id/{pk}', response_model=ResponseModel)
def get_by_id(pk: int, session: Session = Depends(get_db)):
	logger.info(f'pk: {pk}')
	data = _service.get_by_id(session,pk)
	return ResponseModel(code=200, msg="Success", data=data.dict)


@router.post('/task-config/add', response_model=ResponseModel)
def create(obj_in: TaskConfigCreateSchema, session: Session = Depends(get_db)):
	data = _service.create(session,obj_in)
	return ResponseModel(code=200, msg="Success", data=True)


@router.post('/task-config/update', response_model=ResponseModel)
def patch(obj_in: TaskConfigUpdateSchema, session: Session = Depends(get_db)):
	data = _service.update(session,obj_in)
	return ResponseModel(code=200, msg="Success", data=True)


@router.delete('/task-config/delete/{pk}', response_model=ResponseModel)
def delete(pk: int, session: Session = Depends(get_db)):
	data = _service.delete(session,pk)
	return ResponseModel(code=200, msg="Success", data=True)


@router.post('/task-config/start-task/{pk}', response_model=ResponseModel)
def delete(pk: int, session: Session = Depends(get_db)):
	data = _service.start_task(session,pk)
	return ResponseModel(code=200, msg="Success", data=True)

