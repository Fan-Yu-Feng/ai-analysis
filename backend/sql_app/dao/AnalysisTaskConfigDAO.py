# backend/sql_app/dao/AnalysisTaskConfigDAO.py
from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.AnalysisTaskConfigDO import AnalysisTaskConfigDO

class AnalysisTaskConfigDAO(BaseDAO):
    _model = AnalysisTaskConfigDO
    _instance = None