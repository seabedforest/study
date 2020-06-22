"""
Python连接数据库并查询
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
name = input("学生姓名:")
sql="select sname,age,gender from student_back where sname=%s;"
cur.execute(sql,[name])
row=cur.fetchone()
print(row)
#关闭游标和数据库
cur.close()
db.close()