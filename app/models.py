# Description: This file contains the models for the database tables.
# filepaths: /d:/Coding/fastapi/app/models.py
# import libraries
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, func
from .database import Base
from sqlalchemy.orm import relationship

# create Post table
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(255), nullable=False)  
    content = Column(String(255), nullable=False) 
    published = Column(Boolean, server_default='1', nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id" , ondelete="CASCADE") ,nullable=False)

    owner = relationship("User")

# create User table
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    
# create Vote table
class Vote(Base):
    __tablename__ = "votes"
    
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"),primary_key= True ,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),primary_key= True, nullable=False)
    