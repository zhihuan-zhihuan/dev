#!/usr/bin/evn python
# -*- coding:utf-8 -*-
from turtle import pd

'''
特点如下：
1 支援大多数的SQL指令
2 一个档案就是一个数据库。不需要安装数据库服务器软件。

   sqlite 不需要任何数据库引擎

3 完整的Unicode支援（因此没有跨语系的问题）。
4 速度很快。
'''

# sqlalchemy 和pymysql要配合使用 类似mybatis
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1.创建引擎
eng = create_engine("mysql+pymysql://root:12345678@localhost/zhihuan?charset=utf8")
print(eng)

# 2.创建基类
Base = declarative_base()


# 3.创建类

class Student(Base):
    __tablename__ = "users"  # 指定表格名称
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False)
    password = Column(String(32), unique=True)
    nickname = Column(String(32), unique=True)


# 4.创建表格
# Base.metadata.create_all(eng)

# 5.添加记录


Session = sessionmaker(bind=eng)
session = Session()

# student = Student(name = "刘备",email = "110@sq.com")# 创建student对象
# session.add(student) # 添加记录


# session.add_all([
#     Student(name='刘小争',email='120@sq.com'),
#     Student(name='刘大争',email='130@sq.com'),
#     Student(name='小小争',email='150@sq.com')
# ])#批量增加


# 查询操作

student = session.query(Student).first()
print(student.id, student.username, student.password)
student2 = session.query(Student).get(ident=1)  # 使用唯一标示
print(student2.id, student2.username, student2.nickname)

session.commit()  # 提交事务
session.close()



