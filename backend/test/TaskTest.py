#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：ai-comment-analysis 
@File    ：TaskTest.py
@Author  ：yohong
@Date    ：2025/1/10 09:56 
"""

# test/TaskTest.py
import unittest
from unittest.mock import patch, MagicMock
from backend.service.CommentAnalysisTask import CommentAnalysisTask
from backend.sql_app.dataobject.TaskConfigDO import TaskConfigDO
from backend.common.enums import TaskStatusEnum, TaskTypeEnum


class TestCommentAnalysisTask(unittest.TestCase):

	@patch('backend.service.CommentAnalysisTask.CommentAnalysisTask._get_wait_tasks')
	@patch('backend.service.CommentAnalysisTask.CommentAnalysisTask.update_task_status')
	def test_fetch_tasks(self, mock_update_task_status, mock_get_wait_tasks):
		# Mock the return value of _get_wait_tasks
		mock_get_wait_tasks.return_value = [
			TaskConfigDO(id=1, status=TaskStatusEnum.WAIT, task_type=TaskTypeEnum.AnalysisComment, priority=1)
		]
		mock_update_task_status.return_value = 1

		task = CommentAnalysisTask()
		task._fetch_tasks()

		# Assert that the task was updated to PROGRESS
		mock_update_task_status.assert_called_with(1, TaskStatusEnum.WAIT, TaskStatusEnum.PROGRESS)

	@patch('backend.service.CommentAnalysisTask.CommentAnalysisTask.run')
	@patch('backend.service.CommentAnalysisTask.CommentAnalysisTask.update_task_status')
	def test_process_task_mock(self, mock_update_task_status, mock_run):
		# Mock the run method
		mock_run.return_value = None
		task = CommentAnalysisTask()
		task_config = TaskConfigDO(id=1, status=TaskStatusEnum.PROGRESS, task_type=TaskTypeEnum.AnalysisComment)

		task._process_task(task_config)

		# Assert that the task was updated to SUCCESS
		mock_update_task_status.assert_called_with(1, TaskStatusEnum.PROGRESS, TaskStatusEnum.SUCCESS)

	# Mock the run method
	def test_process_task(self):
		# mock_run.return_value = None
		task = CommentAnalysisTask()
		task_config = TaskConfigDO(id=1, status=TaskStatusEnum.PROGRESS, task_type=TaskTypeEnum.AnalysisComment, prompt_config_id = 1)

		task._process_task(task_config)

		# Assert that the task was updated to SUCCESS
		# mock_update_task_status.assert_called_with(1, TaskStatusEnum.PROGRESS, TaskStatusEnum.SUCCESS)


if __name__ == '__main__':
	unittest.main()
