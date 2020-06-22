"""
m 数据库查询数据模型
"""
import pymysql


# 连接数据库
class DataBase:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8")

    # 创建游标
    def cursor(self):
        self.cur = self.db.cursor()

    # 关闭数据库连接
    def close(self):
        self.db.close()

    # =========功能性方法--》提供数据
    # 处理数据库层面的注册功能
    def register(self, name, passwd):
        sql = "insert into user (name,passwd) values (%s,%s);"
        try:
            self.cur.execute(sql, [name, passwd])
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()
            return False

    def login(self, name, passwd):
        # binary 让查询区分大小写
        sql = "select name from user where binary name=%s and binary passwd=%s;"
        self.cur.execute(sql, [name, passwd])
        r = self.cur.fetchone()
        if r:
            return True
        return False

    # 插入历史记录
    def insert_history(self, name, word):
        # id uid history times
        sql = "select id from user where name=%s;"
        self.cur.execute(sql, [name])
        # fetchone() --> (id,)
        uid = self.cur.fetchone()[0]
        sql = "insert into history (uid,history) values (%s,%s);"
        try:
            self.cur.execute(sql, [uid, word])
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()

    # 查询单词
    def query(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        r = self.cur.fetchone()  # 查到 (mean,) 没有 None
        if r:
            return r[0]

    # 历史记录查询
    def history(self, name):
        # name history times
        sql = "select name,history,times from user inner join history \
            on user.id=history.uid where name=%s order by times desc limit 10;"
        self.cur.execute(sql, [name])
        return self.cur.fetchall()  # 结果类型((name,history,times),()..)
