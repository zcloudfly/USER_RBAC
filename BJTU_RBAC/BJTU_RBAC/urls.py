"""BJTU_RBAC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from BJTU_RBAC.view import topage,userview,roleview,permissionview
urlpatterns = [
    #跳转页
    url(r'^rbac/', topage.home),
    url(r'^usertab/', topage.usertab),
    url(r'^roletab/', topage.roletab),
    url(r'^permtab/', topage.permtab),
    url(r'mainPage',topage.mainPage),
    url(r'saveUserPage',topage.saveUserPage),
    url(r'saveRolePage',topage.saveRolePage),
    url(r'savePermPage',topage.savePermPage),
    url(r'toSetRolePage',topage.toSetRolePage),
    url(r'toSetPermPage',topage.toSetPermPage),
    #用户url
    url(r'getUserList',userview.getUserList),
    url(r'deleteUserByid',userview.deleteUserByid),
    url(r'updateUser',userview.updateUser),
    url(r'saveUser',userview.saveUser),
    url(r'userRoles',userview.userRoles),
    #角色url
    url(r'allRoles', roleview.allRoles),
    url(r'roleList', roleview.roleList),
    url(r'userRoleSave', roleview.saveUserRole),
    url(r'getRoleList',roleview.getRoleList),
    url(r'deleteRoleById',roleview.deleteRoleById),
    url(r'updateRole',roleview.updateRole),
    url(r'saveRole',roleview.saveRole),
    #权限url
    url(r'permListcombox',permissionview.permList),
    url(r'getPermList',permissionview.getPermList),
    url(r'deletePermById',permissionview.deletePermById),
    url(r'updatePerm',permissionview.updatePerm),
    url(r'savePerm',permissionview.savePerm),
    url(r'getPermTree',permissionview.getPermTree),
    url(r'getRolePerm',permissionview.getRolePerm),
    url(r'role_PermSave',permissionview.rolePermSave),
]
