#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import pymysql
# 类似JDBC
db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='12345678',
    db='zhihuan',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor  # [{'Tables_in_zhihuan': 'users'}]  默认是元祖
)


def test_conn():
    with db.cursor() as cursor:
        sql = 'show tables;'
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())
