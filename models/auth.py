#!C:\Users\Administrator\Code F:\Anaconda\python.exe 3.6.4
# author: YanYeek  encoding: utf-8
# file: auth.py  time: 2020/5/19 14:08
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__))) # 把项目路径添加到path中
from models.db import Base, session
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class BaseModels:
    is_delete = Column(Boolean, default=False) # 逻辑删除
    update_time = Column(DateTime, default=datetime.now) # 修改
    create_time = Column(DateTime, default=datetime.now) # 创建

class User(Base, BaseModels):
    __tablename__ = 'users'  # 表格名字
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(30), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    activation = Column(Boolean, default=False) # 激活
    email = Column(String(100))
    phone = Column(String(30))
    
    @classmethod
    def add_user(cls, username, password, **kwargs):
        user = User(username=username, password=password, **kwargs)
        session.add(user)
        session.commit()
        session.close()
    
    @classmethod
    def check_username(cls, username):
        return session.query(cls).filter_by(username=username).first()
    
    def __repr__(self):
        return "User:username=%s.password=%s"%(self.username, self.password)
    
class Post(Base, BaseModels):
    __tablename__ = 'posts'  # 表格名字
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(300))
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="posts", uselist=False, cascade="all")
    
    def __repr__(self):
        return "Post:user_id=%s" % self.user_id
    
    @classmethod
    def add_post(cls, image_url, username):
        user = User.check_username(username) # 返回一个user实例
        post = Post(image_url=image_url, user_id=user.id)
        session.add(post)
        session.commit()
        post_id = post.id
        session.close()
        return post_id
        
    
    