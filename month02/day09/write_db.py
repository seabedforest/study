"""
数据库写操作示例
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

# 执行写sql语句 （曾删改）
try:
    # 可以同时执行多条sql写语句之后一次commit,这样效率更高
    # sql = "insert into cls values (6,'Tonny',19,'m',75);"
    # cur.execute(sql)

    sql = "update cls set score=%s where name=%s;"
    cur.execute(sql,[88,'Tonny'])
    db.commit() # 提交写操作
except:
    # 让所有的写操作失效
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()