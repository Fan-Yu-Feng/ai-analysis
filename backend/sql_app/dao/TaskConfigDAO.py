# backend/sql_app/dao/TaskConfigDAO.py
from backend.sql_app.dao.BaseDAO import BaseDAO
from backend.sql_app.dataobject.TaskConfigDO import TaskConfigDO
from backend.sql_app.vo.TaskConfigVO import TaskConfigCreateSchema, TaskConfigUpdateSchema


class TaskConfigDAO(BaseDAO[TaskConfigDO, TaskConfigCreateSchema, TaskConfigUpdateSchema]):
    _model = TaskConfigDO
    _instance = None