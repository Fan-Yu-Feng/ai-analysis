from pydantic import BaseModel


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
	comment_json_extra_: str
	reply_comment_total_: int


class SocialMediaCommentListCreate(SocialMediaCommentList):
	"""
    请求模型验证：
    email:
    password:
    """
	pass


class SocialMediaCommentList(SocialMediaCommentList):
	"""
    响应模型：
    id:
    email:
    is_active
    并且设置orm_mode与之兼容
    """
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
    并且设置orm_mode与之兼容
    """
    id: int
    is_active: bool

    class Config:
        orm_mode = True