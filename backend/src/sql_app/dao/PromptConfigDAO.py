# backend/sql_app/dao/TaskConfigDAO.py
from backend.src.sql_app.dao.BaseDAO import BaseDAO
from backend.src.sql_app.dataobject.PromptConfigDO import PromptConfigDO


class PromptConfigDAO(BaseDAO):
	_model = PromptConfigDO
	_instance = None
