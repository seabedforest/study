"""
1. 将dict.txt中点单词存入到数据库
 创建一个数据库  dict
 create database dict charset=utf8;
 创建数据表     words  字段： id   word   mean
 create table words (
 id int primary key auto_increment,
 word varchar(30),
 mean varchar(512));
 将单词本中单词插入到这个数据表
"""

import pymysql
import re

# 连接数据库 (连接本机数据库host port 可以不写)
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "dict",
                     charset = "utf8")

# 创建游标   （游标：对数据库进行数据操作的对象，可以获取操作结果）
cur = db.cursor()

# 将单词表中内容插入数据库
f = open('dict.txt')

args_list = []
sql = "insert into words (word,mean) values (%s,%s);"
try:
    for line in f:
        l = re.findall(r"(\w+)\s+(.*)",line) # 匹配出单词和解释
        args_list.append(l[0]) # 单词元组放入列表

        # l[0] ---> (word,mean)
        # cur.execute(sql,l[0])
    cur.executemany(sql,args_list)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库
f.close()
cur.close()
db.close()
