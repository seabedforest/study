"""
数据库查询操作演示
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

# 执行查询sql语句
sql = "select name,age,score from cls where score>70;"
cur.execute(sql)

# 每次迭代取值获取一条查询记录
# for row in cur:
#     print(row)

# 获取查询结果的第一条  返回值类型--》  Y ( )   N None
row = cur.fetchone()
print(row)

# 获取查询结果的前n条 返回值类型--》  Y ((),() )   N ()
row = cur.fetchmany(3)
print(row)

# 获取所有查询结果 返回值类型--》  Y ((),() )   N ()
row = cur.fetchall()
print(row)


# 关闭游标和数据库
cur.close()
db.close()