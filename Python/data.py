import json

class Data:
  def __init__(self):
    self.path = "../DataBase/python.json"

  def getData(self, person):
    with open(self.path, "r") as d:
      data = json.loads(d.read())
      print(data)

  def setData(self, data):
    with open(self.path, "w") as g:
      print("Setting Data:", data)
      g.write(data)