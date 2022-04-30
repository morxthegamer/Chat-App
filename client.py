import socket, threading, time

PORT = 9000
HOST = "127.0.0.1"

class Client:
  def __init__(self, host, port):
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client.connect((host, port))
    self.nickname = input("Enter a nickname: ")

  def receive(self):
    while (True):
      try:
        message = self.client.recv(1024).decode("utf-8")
        if message == "NICKNAME REQUEST":
          self.client.send(self.nickname.encode('utf-8'))
        else: print(message)
  
      except Exception as e:
        print(e)
        self.client.close()
        break
  
  def write(self):
    while (True):
      time.sleep(1)
      message = input('💭: ')
      self.client.send(message.encode("utf-8"))

  def start(self):
    receive_thread = threading.Thread(target=self.receive)
    write_thread = threading.Thread(target=self.write)
  
    receive_thread.start()
    write_thread.start()

if __name__ == "__main__":
  client = Client(HOST, PORT)
  client.start()