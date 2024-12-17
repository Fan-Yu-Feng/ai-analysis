import unittest

from fastapi import Depends

import backend.sql_app.social_media_comment_list_curd as social_media_comment_list_crud

from backend.sql_app.database import SessionLocal


# Dependency
def get_db():
	"""
	每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
	:return:
	"""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


class MyTestCase(unittest.TestCase):
	def test_something(self):
		db = SessionLocal()
		db_user = social_media_comment_list_crud.get_social_media_info(db, 1822126883)
		print(db_user)
		try:
			yield db
		finally:
			db.close()


if __name__ == '__main__':

	MyTestCase.test_something()
