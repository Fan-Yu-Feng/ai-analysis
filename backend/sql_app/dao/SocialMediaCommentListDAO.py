from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.SocialMediaCommentListDO import SocialMediaCommentListDO


class SocialMediaCommentListDAO(BaseDAO):
	_instance = None

	def get_auths(self):
		""" 获取所有auth """
		return self.session.query(SocialMediaCommentListDO).all()

	def add(self, do):
		self.session.add(do)
		self.session.flush()

	def get_by_comment_id(self, comment_id=None):
		""" 根据code获取auth """
		return self.session.query(SocialMediaCommentListDO).filter(
			SocialMediaCommentListDO.comment_id_ == comment_id).first()

	def get_paginated_comments(self, page: int, page_size: int, start_id: int = 0):
		offset = (page - 1) * page_size
		return self.session.query(SocialMediaCommentListDO).where(SocialMediaCommentListDO.id_ > start_id ).order_by("id_").limit(page_size).offset(offset).all()
