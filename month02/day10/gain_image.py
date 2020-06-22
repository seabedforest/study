"""
从数据库提取图片
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

# 存储二进制文件  将文件读取为字节串,插入到数据库

sql="select image from cls where id=1;"
cur.execute(sql)
data=cur.fetchone()[0]
with open("aa.jpg", 'wb') as f:
    f.write(data)
#关闭游标和数据库
cur.close()
db.close()