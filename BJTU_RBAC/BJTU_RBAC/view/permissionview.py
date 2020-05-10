import time,datetime,json,uuid,requests
from sqlalchemy import and_,extract
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
import BJTU_RBAC.models as models
from BJTU_RBAC.orm import sqlConn
localtime = time.localtime(time.time())

'''
获取权限角色（分页）
'''
def getPermList(request):
    curPage = int(request.GET.get("curPage"))  # 当前页
    pageSize = int(request.GET.get("pageSize"))  # 每页条数
    PermList = sqlConn.getqueryAll(models.Permission).limit(pageSize).offset((curPage - 1) * pageSize)
    totalSize = sqlConn.getqueryAll(models.Permission).all().__len__()
    Permjoin = ','.join([str(x) for x in PermList])
    totalPageSize = int((totalSize + pageSize - 1) / pageSize)  # 总页数
    jsonstr = {'data': '[' + Permjoin + ']', 'totalSize': totalSize, 'curPage': curPage, 'totalPageSize': totalPageSize}
    return HttpResponse(json.dumps(jsonstr))
'''
删除权限
'''
def deletePermById(request):
    pId=request.GET.get('id')
    sqlConn.deletebyWhere(models.Permission,{'pId':pId})
    return HttpResponse(json.dumps({'status':'OK','msg':'删除成功~'}))
'''
保存权限
'''
def savePerm(request):
    pId=request.POST.get('pId')
    pName = request.POST.get('pName')
    pCode = request.POST.get('pCode')
    parentId = request.POST.get('parentId')
    perm=None
    if pCode!=None:
        perm=sqlConn.getObjBywhere(models.Permission,{'pCode':pCode}).scalar()
    if perm==None:
        perm=models.Permission(pId=uuid.uuid1().__str__().replace('-',''),
                         pCode=pCode,
                         pName=pName,
                         parentId=parentId )
        sqlConn.save(perm)
        return HttpResponse(json.dumps({'status':'OK','msg':'保存成功'}))
    else:
        return HttpResponse(json.dumps({'status': 'error', 'msg': '已经存在的账号'}))
'''
更新权限
'''
def updatePerm(request):
    sqlConn.updatebyWhere(models.Permission,{'pId':request.POST.get('pId')},
                       { 'pCode' : request.POST.get('pCode'),
                         'pName' : request.POST.get('pName'),
                         'parentId': request.POST.get('parentId')
                         })
    return HttpResponse(json.dumps({'status': 'OK', 'msg': '更新成功'}))
'''
查询全部权限
'''
def permList(request):
    LIST = models.sqlConn.getqueryAll(models.Permission).all()
    jsonList= ','.join([str(x) for x in LIST])
    return HttpResponse('['+jsonList+']')

'''
查询全部角色
'''
def allRoles(request):
    accId=request.GET.get('accId')
    userRoles=sqlConn.getObjBywhere(models.UserRole,{'accId':accId})
    roleList=sqlConn.getqueryAll(models.Role).all()
    uR = ','.join([str(x) for x in userRoles])
    rolejoin = ','.join([str(x) for x in roleList])
    return HttpResponse(json.dumps({'roles':'['+rolejoin+']','userRole':'['+uR+']'}))
'''
权限角色关系保存
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
'''
权限树
'''
def getPermTree(request):
    parentId=request.POST.get('id')
    if parentId!=None:
        data=sqlConn.getObjBywhere(models.Permission,{'parentId':parentId})
    else:
        data = sqlConn.getObjBywhere(models.Permission, {'parentId': '00'})
    list=[]
    for x in data:
        ptree=models.PermTree(id=x.pCode,text=x.pName,checked='',children='')
        list.append(ptree)
    jsonList = ','.join([str(x) for x in list])
    return HttpResponse('['+jsonList+']')
'''
获取角色权限
'''
def getRolePerm(request):
    roleId=request.GET.get('roleId')
    rolePerm=sqlConn.getObjBywhere(models.RolePermission,{'roleId':roleId}).all()
    list=[]
    for x in rolePerm:
        perm=sqlConn.getObjBywhere(models.Permission,{'pId':x.pId}).scalar()
        list.append(perm.pCode)
    return HttpResponse(json.dumps(list))
'''
保存角色权限关系表
'''
def rolePermSave(request):
    try:
        roleId=request.POST.get('roleId')
        pCodes=request.POST.get('pCodes')
        split=pCodes.split(',')
        if roleId:
            sqlConn.deletebyWhere(models.RolePermission,{'roleId':roleId})
            for pCode in split:
                if pCode!='':
                    perm=sqlConn.getObjBywhere(models.Permission,{'pCode':pCode}).scalar()
                    rp=models.RolePermission(roleId=roleId,pId=perm.pId)
                    sqlConn.save(rp)
        return HttpResponse(json.dumps({'status': 'OK', 'msg': '保存成功~'}))
    except :
        return HttpResponse(json.dumps({'status': 'error', 'msg': '保存失败~'}))