from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class SocialMediaCommentList(BaseModel):
	platform_: str
	platform_account_id_: str
	platform_media_id_: str
	comment_id_: str
	comment_content_: str
	comment_like_: int
	comment_uid_: str
	comment_sec_uid_: str
	comment_user_nickname_: str
	comment_time_: str
	is_del_: int
	create_by_: int
	create_time_: str
	update_by_: int
	update_time_: str
	update_time_: Optional[str]  # Allow None and expect string
	comment_json_extra_: Optional[str]  # Allow None and expect string


class SocialMediaCommentListCreate(SocialMediaCommentList):
	"""
    请求模型验证：
    email:
    password:
    """
	pass


class SocialMediaCommentList(SocialMediaCommentList):
	id_: int

	class Config:
		from_attributes = True


class UserBase(BaseModel):
	email: str


class UserCreate(UserBase):
	"""
	请求模型验证：
	email:
	password:
	"""
	password: str


class User(UserBase):
	"""
	响应模型：
	id:
	email:
	is_active
	并且设置from_attributes与之兼容
	"""
	id: int
	is_active: bool

	class Config:
		from_attributes = True


class SocialMediaContentInfoBase(BaseModel):
	platform: Optional[str]
	platform_account_id: Optional[str]
	platform_nickname: Optional[str]
	platform_media_id: Optional[str]
	title: Optional[str]
	content: Optional[str]
	comments_count: Optional[int]
	liked_count: Optional[int]
	collected_count: Optional[int]
	link: Optional[str]
	pub_time: Optional[datetime]
	pub_update_time: Optional[datetime]
	is_del_: Optional[int] = 0
	create_by_: int
	create_time_: datetime
	update_by_: Optional[int]
	update_time_: Optional[datetime]
	ext_info: Optional[str]


	class Config:
		from_attributes = True


class SocialMediaContentInfoCreate(SocialMediaContentInfoBase):
	pass


class SocialMediaContentInfo(SocialMediaContentInfoBase):
	id_: int
