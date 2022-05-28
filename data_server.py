import threading, socket

HOST = '127.0.0.1'
PORT = 9000

class Server:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

    def handle_client(self):
        pass
    
    def receive(self):
        pass