#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Desc    : 任务基类
@File    ：BaseTask.py
@Author  ：yohong
@Date    ：2025/1/9 16:16
"""
import threading
import queue
from concurrent.futures import ThreadPoolExecutor
from abc import ABC, abstractmethod

from backend.sql_app.dao.PromptConfigDAO import PromptConfigDAO
from backend.sql_app.dao.TaskConfigDAO import TaskConfigDAO
from backend.sql_app.dataobject.TaskConfigDO import TaskConfigDO


class BaseTask(ABC):
	"""
    处理任务，一般来说我希望有两种方式，
    一种是定时拉取任务，这个方法是私有的，我不希望外部可以调用。
    另外一种是主动推送任务，这个方法是可以提供调用的。
    执行的时候需要保证幂等性，因为可能会重复执行
    同时要保证优先级高的先执行
    执行任务时定义一个线程池，从线程池中去取线程执行任务
    """
	_task_config_dao = TaskConfigDAO.getInstance()
	_prompt_config_dao = PromptConfigDAO.getInstance()

	def __init__(self, max_workers=5):
		"""
		初始化方法
		:param max_workers: 最大线程数
		"""
		self.task_queue = queue.PriorityQueue()
		self.processed_tasks = set()
		self.executor = ThreadPoolExecutor(max_workers=max_workers)
		self.lock = threading.Lock()

	def update_task_status(self, task_id, source_status, target_status, msg: str = None):
		"""
		更新任务状态  target_status -> source_status
		:param target_status: 更新目标状态
		:param source_status:  数据原本的状态
		:param task_id: 任务id
		"""
		update_do = TaskConfigDO(status=target_status)
		if msg:
			update_do.error_message = msg
		return self._task_config_dao.update_by_filters(update_do, id=task_id, status=source_status)

	@abstractmethod
	def _get_wait_tasks(self):
		"""
		获取待处理任务
		"""
		pass

	def _fetch_tasks(self):
		"""
        定时拉取任务，这个方法是私有的
        """
		# Fetch tasks from the source and add to the queue
		# Example: self.task_queue.put((priority, task))
		pass

	def push_task(self, priority, task: TaskConfigDO):
		"""
        主动推送任务，这个方法是可以提供调用的
        :param priority: task priority
        :param task: task object
        """
		with self.lock:
			if task not in self.processed_tasks:
				self.task_queue.put((priority, task))

	def _process_task(self, task):
		"""
        process task
        :param task: task object
        """
		# Implement the actual task processing logic here

		pass

	def _worker(self):
		while True:
			try:
				priority, task = self.task_queue.get()
				with self.lock:
					if task not in self.processed_tasks:
						self.processed_tasks.add(task)
						self._process_task(task)
			finally:
				self.task_queue.task_done()
				self.processed_tasks.remove(task)

	def start(self):
		"""
        Start the task processing
        """
		for _ in range(self.executor._max_workers):
			self.executor.submit(self._worker)

	def start_fetching(self, interval):
		"""
		Start the task fetching
		:param interval:  interval in seconds
		"""
		self._fetch_tasks()
		threading.Timer(interval, self.start_fetching, args=(interval,)).start()

	def stop(self):
		"""
		Stop the task processing
		"""
		self.executor.shutdown()

