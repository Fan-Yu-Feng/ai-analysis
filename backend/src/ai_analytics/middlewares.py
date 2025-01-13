#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：middlewares.py
@Author  ：yohong
@Date    ：2025/1/10 15:04 
"""

from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.exceptions import RequestValidationError

from ai_analytics.sql_app.config.database import SessionLocal

origins = [
	"http://localhost",
	"http://localhost:8080",
	"http://localhost:8848",
]
from fastapi.middleware.cors import CORSMiddleware


async def db_session_middleware(request: Request, call_next: Callable) -> Response:
	response = Response('Internal server error', status_code=500)
	try:
		request.state.db = SessionLocal()
		response = await call_next(request)
	finally:
		request.state.db.close()

	return response


from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from ai_analytics.controller import ResponseModel


async def global_exception_handler(request: Request, exc: Exception):
	if isinstance(exc, HTTPException):
		return JSONResponse(
			status_code=exc.status_code,
			content=ResponseModel(code=exc.status_code, msg=exc.detail, data=None).dict()
		)
	return JSONResponse(
		status_code=500,
		content=ResponseModel(code=500, msg="Internal Server Error", data=None).dict()
	)


def init_middleware(app: FastAPI) -> None:
	app.middleware('http')(db_session_middleware)
	app.add_middleware(
		CORSMiddleware,
		allow_origins=origins,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)
	app.add_exception_handler(Exception, global_exception_handler)
	app.add_exception_handler(RequestValidationError, global_exception_handler)
