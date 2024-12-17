from sqlalchemy import Boolean, Column, Integer, String, BigInteger, DateTime, Text, Index
from backend.sql_app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(32), unique=True, index=True)
    hashed_password = Column(String(32))
    is_active = Column(Boolean, default=True)


class SocialMediaCommentList(Base):
    __tablename__ = "social_media_comment_list"

    id_ = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')
    platform_ = Column(String(50, collation='utf8mb4_general_ci'), nullable=True, comment='平台')
    platform_account_id_ = Column(String(255, collation='utf8mb4_general_ci'), nullable=True, comment='平台账号ID')
    platform_media_id_ = Column(String(200, collation='utf8mb4_general_ci'), nullable=True, comment='视频或文章ID')
    comment_id_ = Column(String(50, collation='utf8mb3_general_ci'), nullable=True, comment='评论ID')
    comment_content_ = Column(String(500, collation='utf8mb4_general_ci'), nullable=True, comment='评论内容')
    comment_like_ = Column(Integer, nullable=True, comment='评论内容点赞数')
    comment_uid_ = Column(String(50, collation='utf8mb3_general_ci'), nullable=True, comment='评论用户ID')
    comment_sec_uid_ = Column(String(100, collation='utf8mb3_general_ci'), nullable=True, comment='评论用户uid')
    comment_user_nickname_ = Column(String(200, collation='utf8mb4_general_ci'), nullable=True, comment='评论用户昵称')
    comment_time_ = Column(DateTime, nullable=True, comment='评论时间')
    is_del_ = Column(Integer, default=0, comment='是否删除')
    create_by_ = Column(BigInteger, nullable=False, comment='创建者')
    create_time_ = Column(DateTime, nullable=False)
    update_by_ = Column(BigInteger, nullable=True)
    update_time_ = Column(DateTime, nullable=True, comment='修改时间')
    comment_json_extra_ = Column(Text(collation='utf8mb4_general_ci'), nullable=True, comment='json字符串')
    reply_comment_total_ = Column(BigInteger, nullable=True, comment='评论回复数量')



    __table_args__ = (
        Index('fk_pk', 'platform_', 'platform_account_id_', 'platform_media_id_', 'comment_id_', mysql_using='BTREE'),
        Index('fk_comment_uid_', 'comment_uid_', mysql_using='BTREE'),
        Index('fk_comment_sec_uid_', 'comment_sec_uid_', mysql_using='BTREE'),
        Index('fk_comment_time_', 'comment_time_', mysql_using='BTREE'),
    )




