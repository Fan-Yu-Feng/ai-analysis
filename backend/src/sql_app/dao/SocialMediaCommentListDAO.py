from backend.src.sql_app.dao.BaseDAO import BaseDAO
from backend.src.sql_app.dataobject.SocialMediaCommentListDO import SocialMediaCommentListDO


class SocialMediaCommentListDAO(BaseDAO):
	_instance = None
	_model = SocialMediaCommentListDO

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

