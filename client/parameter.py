import json


class Parameter(object):
    def __init__(self, jsonData):
        if type(jsonData) is str:
            self.obj = json.loads(jsonData)
        elif type(jsonData) is dict:
            self.obj = jsonData
        self.name = "memcached"

    def getParamStr(self):
        param = ""
        for i, v in self.obj.iteritems():
            param += "-" + i + " " + str(v) + " "
        return param

    def getParamCli(self):
        param = ""
        for i,v in self.obj.iteritems():
            param += "--" + i + "=" + str(v) + " "
        return param
    def addParam(self, k, v):
        self.obj[k] = v

    def setName(self, name):
        self.name = name

    def toJson(self):
        return json.dumps({"name": self.name, "data": self.obj})
