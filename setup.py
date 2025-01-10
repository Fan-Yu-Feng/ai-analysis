#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：server.py
@Author  ：yohong
@Date    ：2025/1/10 15:14 
"""


import uvicorn
from fastapi import FastAPI

from backend import middlewares, routes
from backend.src.config import settings
from backend.src.common.log import init_log


class Server:

    def __init__(self):
        init_log()
        self.app = FastAPI()

    def init_app(self):
        middlewares.init_middleware(self.app)
        routes.init_routers(self.app)

    def run(self):
        self.init_app()
        uvicorn.run(
            app=self.app,
            host=settings.HOST,
            port=settings.PORT,
        )