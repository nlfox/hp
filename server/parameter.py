import json


class Parameter(object):
    def __init__(self, jsonData):
        self.obj = json.loads(jsonData)

    def getParam(self):
        param = ""
        for i, v in self.obj.iteritems():
            param += "-" + i + " " + v + " "
        return param
