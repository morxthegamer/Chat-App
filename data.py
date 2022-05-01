import json, yaml

class Data:
    def __init__(self, path):
        self.path = path

    def getData(self):
        with open(self.path, "r") as d:
            data = json.loads(d.read())
            return data

    def setData(self, data):
        with open(self.path, "w") as g:
            print(f"Setting Data: {data}")
            g.write(json.dumps(data))

    def setChatData(self, data):
        with open(self.path, "w") as j:
            print(f"Setting Data: {data}")
            j.write(yaml.dump(data))