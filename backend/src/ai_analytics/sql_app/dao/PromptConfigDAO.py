# backend/sql_app/dao/PromptConfigDAO.py
from ai_analytics.sql_app.dao.BaseDAO import BaseDAO
from ai_analytics.sql_app.dataobject.PromptConfigDO import PromptConfigDO
from ai_analytics.sql_app.vo.PromptConfigVO import PromptConfigCreateSchema, PromptConfigUpdateSchema


class PromptConfigDAO(BaseDAO[PromptConfigDO, PromptConfigCreateSchema, PromptConfigUpdateSchema]):
	_model = PromptConfigDO
	_instance = None
