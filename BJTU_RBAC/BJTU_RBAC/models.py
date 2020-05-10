from sqlalchemy import Column, Integer, String, DateTime, CHAR
from BJTU_RBAC.orm import sqlConn
import json
Base= sqlConn.Base

class JsonClass(object):
    def to_json_string(self):
        return json.dumps(self,default=lambda obj:obj.__dict__)
    def from_json_string(self,json_string):
        data=json.loads(json_string)
        for key in self.__dict__.keys():
            setattr(self,key,data[key])
'''
用户表
'''
class User(Base):
    __tablename__ = 'User'
    id = Column(String(32), primary_key=True)
    acct = Column(String(32), nullable=True)
    name = Column(String(20), nullable=True)
    ctime = Column(DateTime, nullable=False)
    sts = Column(String(1), nullable=False)
    pwd = Column(String(20), nullable=True)
    def __init__(self, id, acct, name, ctime,sts,pwd):
        self.id = id
        self.acct = acct
        self.name = name
        self.ctime = ctime
        self.sts = sts
        self.pwd = pwd

    def __repr__(self):
        return '{' + '"id":"{}","acct":"{}","name":"{}","ctime":"{}","sts":"{}","pwd":"{}"'.\
            format(self.id, self.acct, self.name,self.ctime,self.sts,self.pwd) + '}'


'''
角色表
'''
class Role(Base):
    __tablename__ = 'Role'
    roleId = Column(String(32), primary_key=True)
    roleName = Column(String(20), nullable=True)
    roleDescribe = Column(String(50), nullable=False)


    def __init__(self, roleId, roleName, roleDescribe):
        self.roleId = roleId
        self.roleName = roleName
        self.roleDescribe = roleDescribe

    def __repr__(self):
        return '{' + '"roleId":"{}","roleName":"{}","roleDescribe":"{}"'. \
            format(self.roleId, self.roleName, self.roleDescribe) + '}'
'''
权限表
'''
class Permission(Base):
    __tablename__ = 'Permission'
    pId = Column(String(32), primary_key=True)
    pCode = Column(String(20), nullable=True)
    pName = Column(String(20), nullable=True)
    parentId = Column(String(32), nullable=False)

    def __init__(self, pId, pCode, pName,parentId):
        self.pId = pId
        self.pCode = pCode
        self.pName = pName
        self.parentId=parentId

    def __repr__(self):
        return '{' + '"pId":"{}","pCode":"{}","pName":"{}","parentId":"{}"'. \
            format(self.pId, self.pCode, self.pName,self.parentId) + '}'

'''
用户角色表
'''
class UserRole(Base):
    __tablename__ = 'User_Role'
    accId = Column(String(32), primary_key=True)
    roleId = Column(String(32), primary_key=True)

    def __init__(self, accId, roleId):
        self.accId = accId
        self.roleId = roleId

    def __repr__(self):
        return '{' + '"accId":"{}","roleId":"{}"'. \
            format(self.accId, self.roleId) + '}'
'''
角色权限表
'''
class RolePermission(Base):
    __tablename__='Role_Permission'
    roleId = Column(String(32), primary_key=True)
    pId = Column(String(32), primary_key=True)

    def __init__(self, pId, roleId):
        self.pId = pId
        self.roleId = roleId

    def __repr__(self):
        return '{' + '"pId":"{}","roleId":"{}"'. \
            format(self.pId, self.roleId) + '}'

'''
权限树数据
'''
class PermTree():
    def __init__(self, id, text, checked,children):
        self.id = id
        self.text = text
        self.checked = checked
        self.children=children
        self.state="open"
    def __repr__(self):
        return '{' + '"id":"{}","text":"{}","checked":"{}","children":"{}","state":"{}"'.\
            format(self.id, self.text, self.checked,self.children,self.state) + '}'

