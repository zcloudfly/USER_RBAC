import json

import BJTU_RBAC.models as models


class JsonClass(object):
    def to_json_string(self):
        return json.dumps(self,default=lambda obj:obj.__dict__)
    def from_json_string(self,json_string):
        data=json.loads(json_string)
        for key in self.__dict__.keys():
            setattr(self,key,data[key])
class Task(JsonClass):
    def __init__(self,id,name):
        self.id=id
        self.name=name


task=Task('1','zhangsan')
user=models.User('1','zhangsan','张三','','','')
print(user.to_json_string())
