import unittest

from backend.src.sql_app.dao import TaskConfigDAO
from backend.src.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO
from backend.src.common.log import logger
from backend.src.sql_app.dataobject import TaskConfigDO


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

	def test_update_by_id(self):
		dao = TaskConfigDAO.getInstance()
		update_data = TaskConfigDO(id=1, status='success')
		result = dao.update_by_id(update_data)
		logger.info(result)
		assert result > 0




if __name__ == '__main__':

	MyTestCase.test_something()
