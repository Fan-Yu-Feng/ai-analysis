#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：routes.py
@Author  ：yohong
@Date    ：2025/1/10 15:05 
"""
from fastapi import APIRouter, FastAPI



def router_v1():
    router = APIRouter()
    router.include_router(views.router, tags=['Article'])
    return router


def init_routers(app: FastAPI):
    app.include_router(router_v1(), prefix='/api/v1', tags=['v1'])