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


def init_middleware(app: FastAPI) -> None:
    app.middleware('http')(db_session_middleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
