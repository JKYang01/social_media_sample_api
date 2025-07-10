from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, JSON, TIMESTAMP, text, Boolean, ForeignKey, DECIMAL

class Post(BaseModel):
    id: Optional[int] = None  # Column(UUID(as_uuid=True),primary_key=True, index=True,default=uuid.uuid4)
    title: str
    content: str
    published: bool = True
    rating: Optional[float] = None