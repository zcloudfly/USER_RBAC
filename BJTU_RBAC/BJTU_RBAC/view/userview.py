import time,datetime,json,uuid,requests
from sqlalchemy import and_,extract
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
import BJTU_RBAC.models as models
from BJTU_RBAC.orm import sqlConn
localtime = time.localtime(time.time())
'''
获取用户列表（分页）条件查询
'''
def getUserList(request):
    curPage = int(request.GET.get("curPage"))  # 当前页
    pageSize = int(request.GET.get("pageSize"))  # 每页条数
    roleId=request.GET.get('roleId')
    pId=request.GET.get('pId')
    User = models.User
    UserRole = models.UserRole
    RoleP = models.RolePermission
    userList=sqlConn.Session_class().query(User)
    if request.GET.get('acct'):
        userList=userList.filter(User.acct==request.GET.get('acct'))
    if request.GET.get('name'):
        userList=userList.filter(User.name==request.GET.get('name'))
    if roleId:
        userList = userList.join(UserRole, User.acct == UserRole.accId).filter(
             UserRole.roleId == roleId)
    if roleId!=''and roleId!=None and pId!=''and pId!=None:
        userList = userList.join(RoleP, UserRole.roleId == RoleP.roleId).filter(
            RoleP.pId == pId)
    elif (roleId==''or roleId==None) and (pId!='' and pId!=None):
        userList = userList.join(UserRole, User.acct == UserRole.accId)\
            .join(RoleP, UserRole.roleId == RoleP.roleId).filter(
            RoleP.pId == pId)
    userList=userList.limit(pageSize).offset((curPage - 1) * pageSize)
    totalSize=userList.all().__len__()
    userjoin = ','.join([str(x) for x in userList])
    totalPageSize = int((totalSize + pageSize - 1) / pageSize)  # 总页数
    jsonstr = {'data': '['+userjoin+']', 'totalSize': totalSize, 'curPage': curPage, 'totalPageSize': totalPageSize}
    return HttpResponse(json.dumps(jsonstr))
'''
删除用户
'''
def deleteUserByid(request):
    id=request.GET.get('id')
    sqlConn.delete(models.User,id)
    return HttpResponse(json.dumps({'status':'OK','msg':'删除成功~'}))
'''
保存用户
'''
def saveUser(request):
    acct=request.POST.get('acct')
    name = request.POST.get('name')
    sts = request.POST.get('sts')
    user=None
    if acct!=None:
       user=sqlConn.getObjBywhere(models.User,{'acct':acct}).scalar()
    if user==None:
        user=models.User(id=uuid.uuid1().__str__().replace('-',''),
                         name=name,
                         sts=sts,
                         acct=acct,
                         pwd= '123456',
                         ctime=localtime)
        sqlConn.save(user)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功'}))
    else:
        return HttpResponse(json.dumps({'status': 'error', 'msg': '已经存在的账号'}))
'''
更新用户
'''
def updateUser(request):
    sqlConn.updateById(models.User,request.POST.get('id'),
                       { 'acct' : request.POST.get('acct'),
                         'name' : request.POST.get('name'),
                         'sts': request.POST.get('sts'),

                         })
    return HttpResponse(json.dumps({'status': 'OK', 'msg': '更新成功'}))
'''
用户角色
'''
def userRoles(request):
    accId = request.GET.get('id')
    userRole=sqlConn.getObjBywhere(models.UserRole,{'accId':accId})
    roleList=[]
    for obj in userRole:
        role=sqlConn.getObjBywhere(models.Role,{'roleId':obj.roleId})[0]
        roleList.append(role)
    userjoin = ','.join([str(x.__repr__()) for x in roleList])
    return HttpResponse('['+userjoin+']')

