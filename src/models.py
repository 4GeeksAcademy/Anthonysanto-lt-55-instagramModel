from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_Name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="post")   
    title: Mapped[str] = mapped_column(String(255), nullable=True)
    media_type: Mapped[str] = mapped_column(String(50), nullable=True)
    media_url: Mapped[str] = mapped_column(String(500), nullable=True)
    content: Mapped[str] = mapped_column(String, nullable=True)


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str] = mapped_column(nullable=False)
    author_id:Mapped[int] = mapped_column(nullable=False) 
    
    post_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="comment")    

class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    user_from_id = mapped_column(ForeignKey("user.id"))
    user = relationship("User", back_populates="follower")
    
    
    user_to_id = mapped_column(ForeignKey("user.id"))