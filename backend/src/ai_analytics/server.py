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
from fastapi.exceptions import RequestValidationError

from ai_analytics import routes, middlewares
from ai_analytics.config import settings
from ai_analytics.common.log import init_log
from ai_analytics.middlewares import global_exception_handler


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


if __name__ == '__main__':
	Server().run()