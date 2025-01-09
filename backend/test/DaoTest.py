import unittest

from backend.sql_app.dao.TaskConfigDAO import TaskConfigDAO
from backend.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO
from backend.common.log import logger
from backend.sql_app.dataobject.TaskConfigDO import TaskConfigDO


class MyTestCase(unittest.TestCase):
	def test_something(self):
		dao = SocialMediaCommentListDAO.getInstance()
		res = dao.get_page_by_start_id(1,10,1822240937)
		logger.info(res)
		assert  res != None

	def test_dao_query_by_filter(self):
		dao = TaskConfigDAO.getInstance()
		res = dao.get_by_filters(status='success')
		logger.info(res)

	def test_dao_query_by_filter_do(self):
		dao = TaskConfigDAO.getInstance()
		res = dao.get_by_filters_do(TaskConfigDO(status='success'))
		logger.info(res)
		assert  res != None

	def test_dao_query_by_id(self):
		dao = TaskConfigDAO.getInstance()
		res = dao.get_by_id(1)
		logger.info(res)
		assert  res != None

	def test_dao_query_all(self):
		dao = TaskConfigDAO.getInstance()
		res = dao.get_all()
		logger.info(res)
		assert  res != None

	def test_dao_query_page_by_start_id(self):
		dao = TaskConfigDAO.getInstance()
		res = dao.get_page_by_start_id(1,10,0)

		logger.info(res)
		assert  res != None

	def test_update_by_id(self):
		dao = TaskConfigDAO.getInstance()
		res = dao.update_by_id(TaskConfigDO(id=1, status='success'))

		logger.info(res)
		assert  res != None


if __name__ == '__main__':

	MyTestCase.test_something()
