from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Text, Index

from backend.src.sql_app.dataobject.BaseDO import BaseDO


class SocialMediaCommentListDO(BaseDO):
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
	comment_json_extra = Column(Text(collation='utf8mb4_general_ci'), nullable=True, comment='json字符串')
	reply_comment_total = Column(BigInteger, nullable=True, comment='评论回复数量')

	__table_args__ = (
		Index('fk_pk', 'platform', 'platform_account_id', 'platform_media_id','comment_id', mysql_using='BTREE'),
		Index('fk_comment_uid','comment_uid', mysql_using='BTREE'),
		Index('fk_comment_sec_uid','comment_sec_uid', mysql_using='BTREE'),
		Index('fk_comment_time','comment_time', mysql_using='BTREE'),
	)
