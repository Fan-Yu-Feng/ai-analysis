# backend/sql_app/dao/TaskConfigDAO.py
from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.TaskConfigDO import TaskConfigDO

class TaskConfigDAO(BaseDAO):
    _model = TaskConfigDO
    _instance = None