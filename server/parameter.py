import json


class Parameter(object):
    def __init__(self, jsonData):
        self.obj = json.loads(jsonData)
        self.program = self.obj["name"]
        self.obj = self.obj["data"]

    def getParam(self):
        param = self.program + " "
        for i, v in self.obj.iteritems():
            param += "-" + i + " " + v + " "
        return param
