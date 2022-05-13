import json

class Data:
    def __init__(self, folder):
        self.folder = folder

    def getData(self, file):
        with open(f"{self.folder}/{file}", "r") as d:
            data = d.read()
            return data

    def setData(self, file, data):
        with open(f"{self.folder}/{file}", "w") as g:
            print(f"Setting Data: {data}")
            g.write(data)

    def getDataJson(self, file):
        with open(f"{self.folder}/{file}", "r") as d:
            data = json.loads(d.read())
            return data

    def setDataJson(self, file, data):
        with open(f"{self.folder}/{file}", "w") as g:
            print(f"Setting Data: {data}")
            g.write(json.dumps(data))