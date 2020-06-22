"""
查询操作2
"""


import pymysql

# 连接数据库 (连接本机数据库host port 可以不写)
db = pymysql.connect(host = "localhost",
                     port = 3306,
                     user = "root",
                     password = "123456",
                     database = "stu",
                     charset = "utf8")

# 创建游标   （游标：对数据库进行数据操作的对象，可以获取操作结果）
cur = db.cursor()

# name = input("Name:")

# 执行查询sql语句
# sql = "select name,score from cls where name='%s';"%name
# print(sql)
# cur.execute(sql)

# 按照位置将列表中数据量传递给sql语句 （不能传递关键字，表名，库名，符号。。。）
sql = "select name,score from cls where sex=%s and score>%s;"
cur.execute(sql,['m',80]) # 给sql语句传递数据参量

row = cur.fetchall()
print(row)


# 关闭游标和数据库
cur.close()
db.close()