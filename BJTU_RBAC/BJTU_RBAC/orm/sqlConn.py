from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine=create_engine("mysql+pymysql://root:123456@localhost/rbac",encoding='utf8',echo=True)
Base=declarative_base()
Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)
#保存单条数据
def save(Object):
    session=Session_class()
    session.add(Object)
    session.commit()
#保存多条数据
def saveAll(Object):
    session=Session_class()
    session.add_all(Object)
    session.commit()
#获取所有数据
def getqueryAll(Object):
    session=Session_class()
    return session.query(Object)
#根据id获取数据
def getqueryById(Object,id):
    session=Session_class()
    return session.query(Object).filter(Object.id == id)
#根据id删除数据
def delete(Object,id):
    session = Session_class()
    session.query(Object).filter(Object.id == id).delete()
    session.commit()

def deletebyWhere(Object, param):
        session = Session_class()
        session.query(Object).filter_by(**param).delete()
        session.commit()
def updatebyWhere(Object, param1, param2):
    session = Session_class()
    session.query(Object).filter_by(**param1).update(param2)
    session.commit()
#根据id更新数据
def updateById(Object,id,param):
    session = Session_class()
    session.query(Object).filter(Object.id == id).update(param)
    session.commit()
def updateById(Object,id,param):
    session = Session_class()
    session.query(Object).filter(Object.id == id).update(param)
    session.commit()

#执行sql
def execute(sql):
    session = Session_class()
    session.execute(sql)
    session.commit()
def executeFetchall(sql):
    session = Session_class()
    list=session.execute(sql).fetchall()
    session.commit()
    return list;
def getObjBywhere(Object,param):
    session = Session_class()
    return session.query(Object).filter_by(**param)