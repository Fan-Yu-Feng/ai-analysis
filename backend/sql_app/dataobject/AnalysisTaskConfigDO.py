# backend/sql_app/dataobject/AnalysisTaskConfigDO.py
from datetime import datetime

from sqlalchemy import Column, BigInteger, Integer, String, Text, DateTime, Boolean, Index
from backend.sql_app.dataobject.BaseDO import BaseDO


class AnalysisTaskConfigDO(BaseDO):
	__tablename__ = 'analysis_task_config'

	prompt_config_id = Column(Integer, nullable=False, comment='评论配置表 id')
	status = Column(String(255), nullable=False, comment='任务状态：待处理、处理中、已完成、失败')
	priority = Column(Integer, default=0, comment='任务优先级，数值越大优先级越高')
	config_detail = Column(Text, comment='配置明细')
	error_message = Column(Text, comment='错误信息，如果任务失败则记录错误信息')
	__table_args__ = (
		Index('idx_prompt_config_id', 'prompt_config_id', mysql_using='BTREE'),
	)
