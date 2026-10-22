from app.db import db 
from sqlalchemy.orm import Mapped,mapped_column,relationship 
from sqlalchemy import func,ForeignKey 
from sqlalchemy_serializer import SerializerMixin 
from datetime import datetime

class Article(db.Model,SerializerMixin):
    __tablename__="articles"

    serialize_rules=("-user.reviews",)

    id:Mapped[int]=mapped_column(primary_key=True)
    author:Mapped[str]
    title:Mapped[str]
    content:Mapped[str]
    preview:Mapped[str]
    minutes_to_read:Mapped[int]
    is_member_only:Mapped[bool]=mapped_column(default=False)
    created_at:Mapped[datetime]=mapped_column(server_default=func.now())

    user_id:Mapped[int]=mapped_column(ForeignKey("users.id"))

    user:Mapped["User"]=relationship(back_populates="articles")


    def __repr__(self):
        return f"<Article {self.id} by {self.author}>"
