"""
mysql.py
pymysql 操作数据库流程示例
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

# 执行各种sql操作


# 关闭游标和数据库
cur.close()
db.close()



