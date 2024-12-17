# 通过id查询用户
from sqlalchemy.orm import Session
import models, schemas


def get_user(db: Session, user_id: int):
	return db.query(models.User).filter(models.User.id == user_id).first()


# 新建用户
def db_create_user(db: Session, user: schemas.UserCreate):
	fake_hashed_password = user.password + "notreallyhashed"
	db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
	db.add(db_user)
	db.commit()  # 提交保存到数据库中
	db.refresh(db_user)  # 刷新
	return db_user


# 通过id查询用户
def get_social_media_info(db: Session, id: int):
	comment = db.query(models.SocialMediaCommentList).filter(models.SocialMediaCommentList.id_ == id).first()
	if comment:
		comment.comment_time_ = comment.comment_time_.strftime('%Y-%m-%d %H:%M:%S') if comment.comment_time_ else None
		comment.create_time_ = comment.create_time_.strftime('%Y-%m-%d %H:%M:%S') if comment.create_time_ else None
		comment.update_time_ = comment.update_time_.strftime('%Y-%m-%d %H:%M:%S') if comment.update_time_ else None
	return comment

# 新建用户
def db_create_social_comment_info(db: Session, social_info: schemas.SocialMediaCommentList):
	db_media = models.SocialMediaCommentList(
		platform_=social_info.platform_,
		platform_account_id_=social_info.platform_account_id_,
		platform_media_id_=social_info.platform_media_id_,
		comment_id_=social_info.comment_id_,
		comment_content_=social_info.comment_content_,
		comment_like_=social_info.comment_like_,
		comment_uid_=social_info.comment_uid_,
		comment_sec_uid_=social_info.comment_sec_uid_,
		comment_user_nickname_=social_info.comment_user_nickname_,
		comment_time_=social_info.comment_time_,
		is_del_=social_info.is_del_,
		create_by_=social_info.create_by_,
		create_time_=social_info.create_time_,
		update_by_=social_info.update_by_,
		update_time_=social_info.update_time_,
		comment_json_extra_=social_info.comment_json_extra_,
		reply_comment_total_=social_info.reply_comment_total_
	)
	db.add(db_media)
	db.commit()  # 提交保存到数据库中
	db.refresh(db_media)  # 刷新
	return db_media
