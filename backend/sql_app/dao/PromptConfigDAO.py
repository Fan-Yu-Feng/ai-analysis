# backend/sql_app/dao/AnalysisTaskConfigDAO.py
from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.PromptConfigDO import PromptConfigDO


class PromptConfigDAO(BaseDAO):
	_model = PromptConfigDO
	_instance = None
