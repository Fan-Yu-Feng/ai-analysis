from typing import List

from backend.sql_app.config.database import SessionLocal
from backend.sql_app.dataobject.BaseDO import BaseDO


def validate_id(id: int):
	""" 校验 id """
	if id is None:
		raise AttributeError("id is required")


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
		raise AttributeError("this method not allowed")

	def get_page_by_start_id(self, page: int, page_size: int, start_id: int = 0):
		if page < 1:
			page = 1
		offset = (page - 1) * page_size
		return self.session.query(self._model).where(self._model.id > start_id).order_by("id").limit(page_size).offset(
			offset).all()

	def add(self, do: BaseDO):
		""" 添加新记录 """
		self.session.add(do)
		self.session.flush()

	def add_all(self, do_list: List[BaseDO]):

		self.session.add_all(do_list)
		self.session.commit()  # 提交保存到数据库中
		self.session.flush()

	def update_by_id(self, data: BaseDO):
		""" 更新记录 """
		validate_id(data.id)
		query = self.session.query(self._model).filter(self._model.id == data.id)
		# session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
		query_obj = {}
		for key, value in data.dict.items():
			if value is not None:
				query_obj[key] = value
		return query.update(query_obj)

	def delete_by_id(self, id: int):
		""" 删除记录 将 deleted 更新为 1 """
		validate_id(id)
		return self._session.query(self._model).filter(self._model.id == id).update({"deleted": 1})

	def get_by_id(self, id: int):
		""" 根据 ID 获取记录 """
		validate_id(id)
		return self.session.query(self._model).filter(self._model.id == id).first()

	def get_by_filters(self, **kwargs):
		""" 根据可变参数获取记录 """
		query = self.session.query(self._model)
		for key, value in kwargs.items():
			query = query.filter(getattr(self._model, key) == value)
		return query.all()

	def get_by_filters_do(self, do: BaseDO):
		""" 根据可变参数获取记录 """
		query = self.session.query(self._model)
		for key, value in do.dict.items():
			if value is not None:
				query = query.filter(getattr(self._model, key) == value)
		return query.all()
