from typing import List
from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.CommentAnalyticsInfoDO import CommentAnalyticsInfoDO
from backend.sql_app.vo.CommentAnalyticsInfoVO import CommentAnalyticsInfoCreate


class CommentAnalyticsInfoDAO(BaseDAO):
	_instance = None

	def get_all(self):
		""" 获取所有记录 """
		return self.session.query(CommentAnalyticsInfoDO).all()

	def add(self, do):
		""" 添加新记录 """
		self.session.add(do)
		self.session.flush()

	def add_all(self, do_list: List[CommentAnalyticsInfoCreate]):
		""" 添加新记录 """
		do_objects = [
			CommentAnalyticsInfoDO(
				comment_id=do.comment_id,
				content=do.content,
				sentiment=do.sentiment,
				topic=do.topic,
				keywords=do.keywords,
				summary=do.summary
			)
			for do in do_list
		]
		self.session.add_all(do_objects)
		self.session.commit()  # 提交保存到数据库中
		self.session.flush()


	def update(self, id, data):
		""" 更新记录 """
		record = self.session.query(CommentAnalyticsInfoDO).filter(CommentAnalyticsInfoDO.id == id).first()
		if record:
			for key, value in data.items():
				setattr(record, key, value)
			self.session.commit()
		return record

	def delete(self, id):
		""" 删除记录 """
		record = self.session.query(CommentAnalyticsInfoDO).filter(CommentAnalyticsInfoDO.id == id).first()
		if record:
			self.session.delete(record)
			self.session.commit()
		return record

	def get_by_id(self, id):
		""" 根据 ID 获取记录 """
		return self.session.query(CommentAnalyticsInfoDO).filter(CommentAnalyticsInfoDO.id == id).first()
