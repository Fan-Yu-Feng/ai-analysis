import unittest
from backend.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO
from backend.common.log import logger


class MyTestCase(unittest.TestCase):
	def test_something(self):
		dao = SocialMediaCommentListDAO.getInstance()
		res = dao.get_page_by_start_id(1,10,1822240937)
		logger.info(res)
		assert  res != None



if __name__ == '__main__':

	MyTestCase.test_something()
