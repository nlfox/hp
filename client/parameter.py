import json


class Parameter(object):
    def __init__(self, jsonData):
        if jsonData is str:
            self.obj = json.loads(jsonData)
        elif jsonData is dict:
            self.obj = jsonData

    def getParamStr(self):
        param = ""
        for i, v in self.obj.iteritems():
            param += "-" + i + " " + str(v) + " "
        return param

    def addParam(self, k, v):
        self.obj[k] = v

    def toJson(self):
        return json.dumps(self.obj)
