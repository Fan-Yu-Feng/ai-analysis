from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class SocialMediaCommentList(BaseModel):
	platform: str
	platform_account_id: str
	platform_media_id: str
	comment_id: str
	comment_content: str
	comment_like: int
	comment_uid: str
	comment_sec_uid: str
	comment_user_nickname: str
	comment_time: str
	deleted: int
	create_by: int
	create_time: str
	update_by: int
	update_time: str
	update_time: Optional[str]  # Allow None and expect string
	comment_json_extra: Optional[str]  # Allow None and expect string


class SocialMediaCommentListCreate(SocialMediaCommentList):
	"""
    请求模型验证：
    email:
    password:
    """
	pass


class SocialMediaCommentList(SocialMediaCommentList):
	id: int

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
	deleted: Optional[int] = 0
	create_by: int
	create_time: datetime
	update_by: Optional[int]
	update_time: Optional[datetime]
	ext_info: Optional[str]


	class Config:
		from_attributes = True


class SocialMediaContentInfoCreate(SocialMediaContentInfoBase):
	pass


class SocialMediaContentInfo(SocialMediaContentInfoBase):
	id: int


