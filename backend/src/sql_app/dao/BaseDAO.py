from typing import List, Optional

from fastapi.encoders import jsonable_encoder

from backend.src.sql_app.config.database import SessionLocal
from backend.src.sql_app.dataobject.BaseDO import BaseDO

from typing import Generic

from backend.src.sql_app.vo.schemas import CreateSchema, ModelType, UpdateSchema


def validate_id(id: int):
	""" 校验 id """
	if id is None:
		raise AttributeError("id is required")


class BaseDAO(Generic[ModelType, CreateSchema, UpdateSchema]):
	_instance = None
	_session = None
	_model = ModelType

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

	def close_session(self):
		if self._session:
			self._session.close()
			self._session = None

	def __del__(self):
		self.close_session()

	def get_all(self):
		""" 获取所有记录 """
		raise AttributeError("this method not allowed")

	def get_page_by_start_id(self, page: int, page_size: int, start_id: int = 0) -> List[ModelType]:
		if page < 1:
			page = 1
		offset = (page - 1) * page_size
		return self.session.query(self._model).where(self._model.id > start_id).order_by("id").limit(page_size).offset(
			offset).all()

	def add(self, obj_in: CreateSchema) -> None:
		""" 添加新记录 """
		obj = self._model(**jsonable_encoder(obj_in))
		self.session.add(obj)
		self.session.flush()

	def add_all(self, obj_list: List[BaseDO]) -> None:
		"""
		添加新记录(批量)
		:param obj_list:
		"""
		do_list = [self._model(**jsonable_encoder(obj)) for obj in obj_list]
		self.session.add_all(do_list)
		self.session.commit()  # 提交保存到数据库中
		self.session.flush()

	def update_by_id(self, data: UpdateSchema) -> int:
		""" 更新记录 """
		validate_id(data.id)
		query = self.session.query(self._model).filter(self._model.id == data.id)
		# session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
		update_obj = {}
		for key, value in data.dict.items():
			if value is not None:
				update_obj[key] = value
		cnt = query.update(update_obj)
		self.session.commit()
		return cnt

	def update_by_filters(self, update_do: BaseDO, **kwargs) -> int:
		""" 更新记录 """
		query = self.session.query(self._model)
		for key, value in kwargs.items():
			query = query.filter(getattr(self._model, key) == value)
		update_obj = {}
		for key, value in update_do.dict.items():
			if value is not None:
				update_obj[key] = value
		cnt = query.update(update_obj)
		self.session.commit()
		return cnt

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
		cnt = query.update(update_obj)
		self.session.commit()
		return cnt

	def delete_by_id_logic(self, id: int) -> int:
		""" 删除记录 将 deleted 更新为 1 逻辑删除
		"""
		validate_id(id)
		query = self._session.query(self._model).filter(self._model.id == id)
		cnt = query.update({"deleted": 1})
		self._session.commit()
		return cnt

	def delete_by_id(self, id: int) -> int:
		""" 删除记录 物理删除
		:param id:  id
		:return:  删除的记录数
		"""
		validate_id(id)
		query = self.session.query(self._model).filter(self._model.id == id)
		cnt = query.delete()
		self.session.commit()
		return cnt

	def get_by_id(self, id: int) -> Optional[ModelType]:
		"""
		根据 id 获取
		:param id:  id
		:return:  BaseDO
		"""
		validate_id(id)
		return self.session.query(self._model).filter(self._model.id == id).first()

	def get_by_filters(self, **kwargs) -> List[ModelType]:
		""" 根据可变参数获取记录 """
		query = self.session.query(self._model)
		for key, value in kwargs.items():
			query = query.filter(getattr(self._model, key) == value)
		return query.all()

	def get_by_filters_do(self, do: BaseDO) -> List[ModelType]:
		""" 根据可变参数获取记录 """
		query = self.session.query(self._model)
		for key, value in do.dict.items():
			if value is not None:
				query = query.filter(getattr(self._model, key) == value)
		return query.all()

	def count(self) -> int:
		""" 统计记录数 """
		return self.session.query(self._model).count()
