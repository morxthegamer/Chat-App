import socket, threading, time

class Client:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = input("Enter a nickname: ")
        self.receive_thread = threading.Thread(target=self.receive)
        self.write_thread = threading.Thread(target=self.write)

    def receive(self):
        while (True):
            try:
                message = self.client.recv(1024).decode("utf-8")

                if message == "NICKNAME REQUEST":
                    self.client.send(self.nickname.encode('utf-8'))
                else: print(message)
        
            except Exception as e:
                print(e)
                break
    
    def write(self):
        while (True):
            try:
                time.sleep(1)
                message = input('Type a message:\n >')
                self.client.send(message.encode("utf-8"))
            except Exception as e:
                print(e)
                break

    def start(self):
        self.receive_thread.start()
        self.write_thread.start()
        exit(0)