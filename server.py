import threading, socket, time

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

        if (message == '!leave'):
          client.send('Exiting. Thank you for chatting!'.encode('utf-8'))
          self.broadcast(f'{self.nicknames[self.clients.index(client)]} has left the chat.')
          index = self.clients.index(client)
          client.close()
          self.clients.remove(client)
          self.nicknames.remove(index)
        
        self.broadcast(f"{self.nicknames[self.clients.index(client)]}: {message}".encode("utf-8"))
          
      except Exception as e:
        index = self.clients.index(client)
        client.close()
        self.clients.remove(client)
        self.nicknames.remove(index)
        break
    
  def receive(self):
    while (True):
      client, address = self.server.accept()
      print(f"Connnected with address: {str(address)}!")
  
      client.send("NICKNAME REQUEST".encode("utf-8"))
      nickname = client.recv(1024).decode("utf-8")
  
      self.clients.append(client)
      self.nicknames.append(nickname)
  
      print(f"Client's nickname is: {nickname}.")
      self.broadcast(f"{nickname} has joined the chat!\n".encode("utf-8"))
      client.send("Connected to server!\n".encode("utf-8"))

      self.receive_thread = threading.Thread(target=self.handle_client, args=(client,))
      self.receive_thread.start()
  
  def start(self):
    print(f"Server is listening! On {self.host}...")
    self.receive()

server = Server('127.0.0.1', 9000)
server.start()