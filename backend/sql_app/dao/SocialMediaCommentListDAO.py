from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.SocialMediaCommentListDo import SocialMediaCommentListDO


class SocialMediaCommentListDAO(BaseDAO):
    _instance = None
    """ 权限相关原子操作 """
    def get_auths(self):
        """ 获取所有auth """
        return self.session.query(SocialMediaCommentListDO).all()

    def add(self, do):
        self.session.add(do)
        self.session.flush()

    def get_by_comment_id(self, comment_id=None):
        """ 根据code获取auth """
        return self.session.query(SocialMediaCommentListDO).filter(SocialMediaCommentListDO.comment_id_ == comment_id).first()
