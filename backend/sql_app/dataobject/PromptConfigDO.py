# backend/sql_app/dataobject/PromptConfigDO.py
from datetime import datetime
from sqlalchemy import Column, BigInteger, Integer, String, Text, DateTime, Boolean
from backend.sql_app.dataobject.BaseDO import BaseDO

class PromptConfigDO(BaseDO):
    __tablename__ = 'prompt_config'

    sentiment = Column(String(255), nullable=False, comment='情感倾向：正面、负面、中性')
    topic = Column(String(255), comment='主要主题')
    summary = Column(String(255), nullable=False, comment='总结类：对产品的看法、对营销手段的评论、表达向往、表达讽刺、其他')
    ext_info = Column(Text, comment='扩展字段，存储其他的 prompt')
    system_prompt = Column(Text, comment='系统 prompt')
    user_prompt = Column(Text, comment='用户 prompt')
    deleted = Column(Boolean, nullable=False, default=False, comment='逻辑删除标志，0 表示未删除，1 表示已删除')
    create_by = Column(String(255), nullable=False, comment='创建人')
    update_by = Column(String(255), nullable=False, comment='修改人')
    create_time = Column(DateTime, default=lambda: datetime.utcnow(), comment='创建时间')
    update_time = Column(DateTime, default=lambda: datetime.utcnow(), onupdate=lambda: datetime.utcnow(), comment='更新时间')