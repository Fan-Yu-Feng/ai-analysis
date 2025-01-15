from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CommentAnalyticsInfoBase(BaseModel):
    comment_id: int
    sentiment: str
    topic: Optional[str] = None
    keywords: Optional[List[str]] = None
    summary: str

class CommentAnalyticsInfoCreate(CommentAnalyticsInfoBase):
    pass

class CommentAnalyticsInfo(CommentAnalyticsInfoBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True