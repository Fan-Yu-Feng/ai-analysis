from backend.sql_app.config.database import SessionLocal
from backend.sql_app.dao.DAOMeta import DAOMeta
from backend.sql_app.dataobject.BaseDO import BaseDO


class BaseDAO():
	_instance = None
	_session = None
	_model = BaseDO

	@classmethod
	def getInstance(cls):
		if cls._instance is None:
			cls._instance = cls()
		return cls._instance

	@property
	def session(self):
		if self._session is None:
			self._session = SessionLocal()
		return self._session

	def get_all(self):
		""" 获取所有记录 """
		return self.session.query(self._model).all()

	def get_page_by_start_id(self, page: int, page_size: int, start_id: int = 0):
		if page < 1:
			page = 1
		offset = (page - 1) * page_size
		return self.session.query(self._model).where(self._model.id > start_id).order_by("id").limit(page_size).offset(
			offset).all()
