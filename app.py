from client import Client

class App:
    def __init__(self):
      self.host = '127.0.0.1'
      self.port = 9000
      self.client = Client(self.host, self.port)

    def start(self):
      self.client.start()