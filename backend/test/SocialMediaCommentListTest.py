import unittest



from backend.sql_app.config.database import SessionLocal
from backend.sql_app.dao.SocialMediaCommentListDAO import SocialMediaCommentListDAO


class MyTestCase(unittest.TestCase):
	def test_something(self):
		dao = SocialMediaCommentListDAO.getInstance()
		res = dao.get_by_comment_id(7164752915994313475)
		print(res)
		assert  res != None



if __name__ == '__main__':

	MyTestCase.test_something()
