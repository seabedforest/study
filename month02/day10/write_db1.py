"""
executemany 示例
批量执行写操作
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

# 插入多条记录
l = [
    ('Dave',16,'m',81),
    ('Ala',17,'w',82),
    ('Levi',18,'m',83),
    ('Han',19,'w',84)
]
sql = "insert into cls (name,age,sex,score) values (%s,%s,%s,%s);"

try:
    # for i in l:
    #     cur.execute(sql,i)

    # 执行多次sql语句，执行次数由列表中的元组个数而定
    cur.executemany(sql,l)
    db.commit()
except:
    db.rollback()


# 关闭游标和数据库
cur.close()
db.close()
