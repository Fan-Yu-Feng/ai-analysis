from sqlalchemy import Boolean, Column, Integer, String, BigInteger, DateTime, Text, Index
from ai_analytics.sql_app.config.database import Base


class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True, index=True)
	email = Column(String(32), unique=True, index=True)
	hashed_password = Column(String(32))
	is_active = Column(Boolean, default=True)


class SocialMediaCommentList(Base):
	# 评论数据表
	__tablename__ = "social_media_comment_list"

	id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')
	platform = Column(String(50, collation='utf8mb4_general_ci'), nullable=True, comment='平台')
	platform_account_id = Column(String(255, collation='utf8mb4_general_ci'), nullable=True, comment='平台账号ID')
	platform_media_id = Column(String(200, collation='utf8mb4_general_ci'), nullable=True, comment='视频或文章ID')
	comment_id = Column(String(50, collation='utf8mb3_general_ci'), nullable=True, comment='评论ID')
	comment_content = Column(String(500, collation='utf8mb4_general_ci'), nullable=True, comment='评论内容')
	comment_like = Column(Integer, nullable=True, comment='评论内容点赞数')
	comment_uid = Column(String(50, collation='utf8mb3_general_ci'), nullable=True, comment='评论用户ID')
	comment_sec_uid = Column(String(100, collation='utf8mb3_general_ci'), nullable=True, comment='评论用户uid')
	comment_user_nickname = Column(String(200, collation='utf8mb4_general_ci'), nullable=True, comment='评论用户昵称')
	comment_time = Column(DateTime, nullable=True, comment='评论时间')
	deleted = Column(Integer, default=0, comment='是否删除')
	create_by = Column(BigInteger, nullable=False, comment='创建者')
	create_time = Column(DateTime, nullable=False)
	update_by = Column(BigInteger, nullable=True)
	update_time = Column(DateTime, nullable=True, comment='修改时间')
	comment_json_extra = Column(Text(collation='utf8mb4_general_ci'), nullable=True, comment='json字符串')
	reply_comment_total = Column(BigInteger, nullable=True, comment='评论回复数量')

	__table_args__ = (
		Index('fk_pk', 'platform_', 'platform_account_id_', 'platform_media_id_', 'comment_id_', mysql_using='BTREE'),
		Index('fk_comment_uid_', 'comment_uid_', mysql_using='BTREE'),
		Index('fk_comment_sec_uid_', 'comment_sec_uid_', mysql_using='BTREE'),
		Index('fk_comment_time_', 'comment_time_', mysql_using='BTREE'),
	)


class SocialMediaContentInfo(Base):
	__tablename__ = 'social_media_content_info'

	id = Column(BigInteger, primary_key=True, autoincrement=True, comment='ID')
	platform = Column(String(50), nullable=True, comment='平台')
	platform_account_id = Column(String(255), nullable=True, comment='平台账号ID')
	platform_nickname = Column(String(255), nullable=True, comment='平台账号昵称')
	platform_media_id = Column(String(200), nullable=True, comment='视频或文章ID')
	title = Column(String(50), nullable=True, comment='文章标题')
	content = Column(String(500), nullable=True, comment='文章内容')
	comments_count = Column(Integer, nullable=True, comment='评论数量')
	liked_count = Column(Integer, nullable=True, comment='点赞数量、喜欢数量')
	collected_count = Column(Integer, nullable=True, comment='收藏数量')
	link = Column(String(255), nullable=True, comment='链接地址')
	pub_time = Column(DateTime, nullable=True, comment='文章发布时间')
	pub_update_time = Column(DateTime, nullable=True, comment='文章更新时间')
	deleted = Column(Integer, default=0, comment='是否删除')
	create_by = Column(BigInteger, nullable=False, comment='创建者')
	create_time = Column(DateTime, nullable=False)
	update_by = Column(BigInteger, nullable=True)
	update_time = Column(DateTime, nullable=True, comment='修改时间')
	ext_info = Column(Text, nullable=True, comment='json字符串')
