#!C:\Users\Administrator\Code F:\Anaconda\python.exe 3.6.4
# author: YanYeek  encoding: utf-8
# file: db.py  time: 2020/5/19 14:09
# 1.首先建立一个空py文件（这里命名为connect.py），导入包：
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 接下来设定连接数据库（以MySQL为例）所需要的信息，包括用户名、密码、端口号、IP以及要使用的数据库名字等信息，例如：
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'instagram'
USERNAME = 'root'
PASSWORD = 'qwe123'
# 然后设置一个字符串的格式：
db_url='mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    DATABASE
)
# 创建一个引擎：
engine = create_engine(db_url)

# 将引擎作为参数导入declarative_base()方法，返回一个类：
Base = declarative_base(engine)

# 同时需要创建一个会话窗，即映射：
Session = sessionmaker(engine)
session = Session()


if __name__=='__main__':
    print(dir(Base))
    print(dir(session))


