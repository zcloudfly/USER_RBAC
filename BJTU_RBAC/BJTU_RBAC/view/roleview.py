import time,datetime,json,uuid,requests
from sqlalchemy import and_,extract
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
import BJTU_RBAC.models as models
from BJTU_RBAC.orm import sqlConn
localtime = time.localtime(time.time())

'''
获取角色角色（分页）
'''
def getRoleList(request):
    curPage = int(request.GET.get("curPage"))  # 当前页
    pageSize = int(request.GET.get("pageSize"))  # 每页条数
    roleList = sqlConn.getqueryAll(models.Role).limit(pageSize).offset((curPage - 1) * pageSize)
    totalSize = sqlConn.getqueryAll(models.Role).all().__len__()
    rolejoin = ','.join([str(x) for x in roleList])
    totalPageSize = int((totalSize + pageSize - 1) / pageSize)  # 总页数
    jsonstr = {'data': '[' + rolejoin + ']', 'totalSize': totalSize, 'curPage': curPage, 'totalPageSize': totalPageSize}
    return HttpResponse(json.dumps(jsonstr))
'''
删除角色
'''
def deleteRoleById(request):
    roleId=request.GET.get('id')
    sqlConn.deletebyWhere(models.Role,{'roleId':roleId})
    return HttpResponse(json.dumps({'status':'OK','msg':'删除成功~'}))
'''
保存角色
'''
def saveRole(request):
    roleId=request.POST.get('roleId')
    roleName = request.POST.get('roleName')
    roleDescribe = request.POST.get('roleDescribe')
    role=None
    if roleId!=None:
       role=sqlConn.getObjBywhere(models.Role,{'roleId':roleId}).scalar()
    if role==None:
        role=models.Role(roleId=roleId,
                         roleName=roleName,
                         roleDescribe=roleDescribe)
        sqlConn.save(role)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功'}))
    else:
        return HttpResponse(json.dumps({'status': 'error', 'msg': '已经存在的账号'}))
'''
更新角色
'''
def updateRole(request):
    sqlConn.updatebyWhere(models.Role,{'roleId':request.POST.get('roleId')},
                       { 'roleName' : request.POST.get('roleName'),
                         'roleDescribe' : request.POST.get('roleDescribe')
                         })
    return HttpResponse(json.dumps({'status': 'OK', 'msg': '更新成功'}))

'''
查询全部角色和用户已有角色
'''
def allRoles(request):
    accId=request.GET.get('accId')
    userRoles=sqlConn.getObjBywhere(models.UserRole,{'accId':accId})
    roleList=sqlConn.getqueryAll(models.Role).all()
    uR = ','.join([str(x) for x in userRoles])
    rolejoin = ','.join([str(x) for x in roleList])
    return HttpResponse(json.dumps({'roles':'['+rolejoin+']','userRole':'['+uR+']'}))
'''
查询全部角色
'''
def roleList(request):
    LIST = models.sqlConn.getqueryAll(models.Role).all()
    jsonList= ','.join([str(x) for x in LIST])
    return HttpResponse('['+jsonList+']')
'''
角色角色关系保存
'''
def saveUserRole(request):
    try:
        accId=request.POST.get('acct')
        roleIds  =request.POST.getlist('roleId')
        if roleIds:
            sqlConn.deletebyWhere(models.UserRole,{'accId':accId})
            for roleId in roleIds:
                ur=models.UserRole(accId=accId,roleId=roleId)
                sqlConn.save(ur)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功~'}))
    except :
        return HttpResponse(json.dumps({'status': 'error', 'msg': '保存失败~'}))


