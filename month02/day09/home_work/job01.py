"""
将dict.txt中点单词存入到数据库
     创建一个数据库  dict
     创建数据表     words  字段： id   word   mean
     将单词本中单词插入到这个数据表
@author hailin
@date 2020-06-08
"""
import re
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="dict",
                     charset="utf8")

# 创建游标
cur = db.cursor()

# 执行各种sql操作
f = open("../dict.txt")
sql ="insert into words(id,word,mean) values (%s,%s,%s)"
n=0
try:
    for line in f:
        n +=1
        repx = r"(\b[a-zA-Z]+)(.+)"
        word=re.search(repx,line).group(1).strip()
        mean=re.search(repx,line).group(2).strip()
        cur.executemany(sql,[(n,word,mean)])
    db.commit()
except:
    db.rollback()
f.close()
#关闭游标和数据库
cur.close()
db.close()
