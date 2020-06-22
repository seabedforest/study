"""
基于SQLAIchemy的CRUD
@author hailai
@date 2020-06-21
"""
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建了一个 BaseModel 类，这个类的子类可以自动与一个表关联
Base = declarative_base()


class Interest(Base):
    __tablename__ = 'interest'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    sex = Column(String(5))
    hobby = Column(String(32))
    price = Column(Integer)
    remark = Column(String(512))


def insert(session):
    """
    插入数据库数据
    :param session: 数据库会话
    :return: None
    """
    data = [Interest(id=1, name='Tom', sex='男', hobby='sing,draw', price=4545, remark="骨骼惊奇,灵魂画手"),
            Interest(id=2, name='Lucy', sex='女', hobby='dance', price=3500, remark="身体轻柔,软若无骨")]
    session.add_all(data)
    session.commit()
    session.rollback()


def update(session):
    """
    更新某条记录
    :param session: 数据库会话
    :return: None
    """""
    data = session.query(Interest).filter(Interest.id == 1).one()
    data.name = 'Jim'
    session.commit()


def select(session):
    """
    查询记录
    :param session: 数据库会话
    :return: None
    """
    data = session.query(Interest).filter().all()
    #print(data)
    for i in data:
        print(i.id, i.name, i.sex, i.hobby, i.price, i.remark)


def delete(session):
    """
    删除某条记录
    :param session: 数据库会话
    :return: None
    """
    session.query(Interest).filter(Interest.id == 1).delete()
    session.commit()


def main():
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/stu')
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    # 创建上面所描述的表interest
    Base.metadata.create_all(engine)
    insert(session)
    update(session)
    select(session)
    delete(session)


if __name__ == '__main__':
    main()
