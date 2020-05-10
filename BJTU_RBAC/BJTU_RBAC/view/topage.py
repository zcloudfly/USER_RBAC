import time,datetime,json,uuid,requests
from sqlalchemy import and_,extract
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.core import serializers
import BJTU_RBAC.models as models
from BJTU_RBAC.orm import sqlConn
localtime = time.localtime(time.time())

'''
系统入口主页
'''
def home(request):
    return render(request,'home.html')
'''
tab主页
'''
def mainPage(request):
    return render(request, 'mainPage.html')
'''
用户tab
'''
def usertab(request):
    return render(request, 'usertab.html')
'''
角色tab
'''
def roletab(request):
    return render(request, 'roletab.html')
'''
权限tab
'''
def permtab(request):
    return render(request, 'permtab.html')
'''
用户添加、修改页
'''
def saveUserPage(request):
    user=None
    id=request.GET.get('id')
    if id!=None:
        user=sqlConn.getqueryById(models.User,id)[0]
    return render(request,'saveUserPage.html',{'user':user})
'''
用户角色分配页面
'''
def toSetRolePage(request):
    user = None
    id = request.GET.get('id')
    if id != None:
        user = sqlConn.getqueryById(models.User, id)[0]
    return render(request, 'setUserRolePage.html', {'user': user})
'''
角色添加、修改页
'''
def saveRolePage(request):
    role=None
    roleId=request.GET.get('roleId')
    if roleId!=None:
        role=sqlConn.getObjBywhere(models.Role,{'roleId':roleId}).scalar()
    return render(request,'saveRolePage.html',{'role':role})
'''
权限添加、修改页
'''
def savePermPage(request):
    perm=None
    pId=request.GET.get('pId')
    if pId!=None:
        perm=sqlConn.getObjBywhere(models.Permission,{'pId':pId}).scalar()
    return render(request,'savePermPage.html',{'perm':perm})
'''
角色权限分配页面
'''
def toSetPermPage(request):
    role = None
    id = request.GET.get('id')
    if id != None:
        role = sqlConn.getObjBywhere(models.Role,{'roleId':id})[0]
    return render(request, 'setRolePermPage.html', {'role': role})