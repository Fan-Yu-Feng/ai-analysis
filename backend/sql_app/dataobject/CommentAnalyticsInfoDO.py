from sqlalchemy import Column, Integer, String, Text, JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from backend.sql_app.config.database import Base


class CommentAnalyticsInfoDO(Base):
    __tablename__ = 'comment_analytics_info'

    id = Column(Integer, primary_key=True, nullable=False, comment='评论的唯一标识符')
    comment_id = Column(Integer, nullable=False, comment='原始评论数据的 id')
    content = Column(Text, nullable=False, comment='评论的内容')
    sentiment = Column(String(255), nullable=False, comment='情感倾向：正面、负面、中性')
    topic = Column(String(255), nullable=True, comment='主要主题')
    keywords = Column(JSON, nullable=True, comment='关键词')
    summary = Column(String(255), nullable=False, comment='总结分类：对产品的看法、对营销手段的评论、表达向往、表达讽刺、其他')
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp(), comment='创建时间')
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp(), comment='更新时间')
