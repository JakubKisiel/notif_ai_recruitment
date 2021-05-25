# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    iduser = Column(Integer, primary_key=True, server_default=text("nextval('users_iduser_seq'::regclass)"))
    username = Column(Text, nullable=False)
    hashedpassword = Column(Text, nullable=False)
    passwordsalt = Column(Text, nullable=False)


class Post(Base):
    __tablename__ = 'posts'

    idpost = Column(Integer, primary_key=True, server_default=text("nextval('posts_idpost_seq'::regclass)"))
    iduser = Column(ForeignKey('users.iduser'), nullable=False)
    postcontent = Column(String(160), nullable=False)
    viewscounter = Column(Integer, nullable=False, server_default=text("0"))

    user = relationship('User')
