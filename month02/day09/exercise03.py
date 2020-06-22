"""
Python连接数据库并修改记录
"""
import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 创建游标
cur = db.cursor()

# 执行各种sql操作
try:
    sql = "insert into student values (6,'煎蛋','male',1,18);"
    cur.execute(sql)
    db.commit()
except:
    db.rollback()
#关闭游标和数据库
cur.close()
db.close()