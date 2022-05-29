import threading, socket

HOST = '127.0.0.1'
PORT = 9000

class Server:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
    
        self.clients = []
        self.nicknames = []
    
    def broadcast(self, message):
        for client in self.clients:
            client.send(message)
    
    def handle_client(self, client):
        while (True):
            try:
                message = client.recv(1024).decode("utf-8")
                self.broadcast(f"{self.nicknames[self.clients.index(client)]}: {message}".encode("utf-8"))
            except Exception as e:
                index = self.clients.index(client)
                client.close()
                self.clients.remove(client)
                self.nicknames.remove(self.nicknames[index])
                break
        
    def receive(self):
        while (True):
            client, address = self.server.accept()
            print(f"Connnected with address: {str(address)}!")
        
            client.send("NICKNAME REQUEST".encode("utf-8"))
            nickname = client.recv(1024).decode("utf-8")

            client.send('BADGE REQUEST'.encode('utf-8'))
            badge = client.recv(1024).decode('utf-8')
        
            self.clients.append(client)
            self.nicknames.append(f'{badge} {nickname}')
        
            print(f"Client's nickname is: {nickname}.")
            self.broadcast(f"{nickname} has joined the chat!\n".encode("utf-8"))
            client.send("Connected to server!\n".encode("utf-8"))
        
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()
    
    def start(self):
        print(f"Server is listening! On {HOST}...")
        self.receive()

if __name__ == "__main__":
    server = Server(HOST, PORT)
    server.start()