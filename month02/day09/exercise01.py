"""
第一次用Python连接数据库并操作
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
sql1 = "select * from student;"
sql2 = "show tables;"
# cur.execute(sql2)
cur.execute(sql1)
#每次迭代取值获取一条查询记录

# for row in cur:
#     print(row)

# for row in cur:
#     print(row)

# row=cur.fetchone()
# print(row)

# row = cur.fetchmany(2)
# print(row)

row = cur.fetchall()
print(row)
#关闭游标和数据库
cur.close()
db.close()