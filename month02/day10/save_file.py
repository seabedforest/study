"""
文件以二进制存储到数据库
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

# 存储二进制文件  将文件读取为字节串，插入到数据库
# with open("timg.jpg",'rb') as f:
#     data = f.read() # data为图片的字节串数据
#
# try:
#     sql = "update cls set image=%s where id=1;"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()

# 从数据库提取文件 查询提取二进制数据，写入文件
sql = "select image from cls where id=1;"
cur.execute(sql)
data = cur.fetchone()[0] # (image,)
with open("bb.jpg",'wb') as f:
    f.write(data)

# 关闭游标和数据库
cur.close()
db.close()