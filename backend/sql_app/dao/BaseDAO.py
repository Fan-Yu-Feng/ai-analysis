from typing import List

from backend.sql_app.config.database import SessionLocal
from backend.sql_app.dataobject.BaseDO import BaseDO

from typing import TypeVar, Generic

def validate_id(id: int):
	""" 校验 id """
	if id is None:
		raise AttributeError("id is required")
T = TypeVar('T')


class BaseDAO(Generic[T]):
	_instance = None
	_session = None
	_model = BaseDO

	@classmethod
	def getInstance(cls) :
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

	def get_page_by_start_id(self, page: int, page_size: int, start_id: int = 0) -> List[T]:
		if page < 1:
			page = 1
		offset = (page - 1) * page_size
		return self.session.query(self._model).where(self._model.id > start_id).order_by("id").limit(page_size).offset(
			offset).all()

	def add(self, do: BaseDO) -> None:
		""" 添加新记录 """
		self.session.add(do)
		self.session.flush()

	def add_all(self, do_list: List[BaseDO]) -> None:
		"""
		添加新记录(批量)
		:param do_list:
		"""
		self.session.add_all(do_list)
		self.session.commit()  # 提交保存到数据库中
		self.session.flush()

	def update_by_id(self, data: BaseDO) -> int:
		""" 更新记录 """
		validate_id(data.id)
		query = self.session.query(self._model).filter(self._model.id == data.id)
		# session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
		update_obj = {}
		for key, value in data.dict.items():
			if value is not None:
				update_obj[key] = value
		return query.update(update_obj)

	def update_by_filters(self, update_do: BaseDO, **kwargs) -> int:
		""" 更新记录 """
		query = self.session.query(self._model)
		for key, value in kwargs.items():
			query = query.filter(getattr(self._model, key) == value)
		update_obj = {}
		for key, value in update_do.dict.items():
			if value is not None:
				update_obj[key] = value
		return query.update(update_obj)

	def update_by_filters_do(self, update_data: BaseDO, req_do: BaseDO) -> int:
		""" 更新记录 """
		query = self.session.query(self._model)
		for key, value in req_do.dict.items():
			if value is not None:
				query = query.filter(getattr(self._model, key) == value)
		update_obj = {}
		for key, value in update_data.dict.items():
			if value is not None:
				update_obj[key] = value
		return query.update(update_obj)

	def delete_by_id(self, id: int) -> int:
		""" 删除记录 将 deleted 更新为 1 """
		validate_id(id)
		return self._session.query(self._model).filter(self._model.id == id).update({"deleted": 1})

	def get_by_id(self, id: int) -> T:
		"""
		根据 id 获取
		:param id:  id
		:return:  BaseDO
		"""

		validate_id(id)
		return self.session.query(self._model).filter(self._model.id == id).first()

	def get_by_filters(self, **kwargs) -> List[T]:
		""" 根据可变参数获取记录 """
		query = self.session.query(self._model)
		for key, value in kwargs.items():
			query = query.filter(getattr(self._model, key) == value)
		return query.all()

	def get_by_filters_do(self, do: BaseDO) -> List[T]:
		""" 根据可变参数获取记录 """
		query = self.session.query(self._model)
		for key, value in do.dict.items():
			if value is not None:
				query = query.filter(getattr(self._model, key) == value)
		return query.all()
