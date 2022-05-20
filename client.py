import socket, threading, time
from data import Data
from termcolor import cprint

class Client:
    def __init__(self, host, port, nickname, theme, badge, text):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = nickname
        self.theme, self.badge, self.text = theme, badge, text
        self.receive_thread = threading.Thread(target=self.receive)
        self.write_thread = threading.Thread(target=self.write)

    def receive(self):
        while (True):
            try:
                message = self.client.recv(1024).decode("utf-8")

                if message == "NICKNAME REQUEST":
                    self.client.send(self.nickname.encode('utf-8'))
                elif message == 'BADGE REQUEST':
                    self.client.send(self.badge.encode('utf-8'))
                else: cprint(message, self.theme)
        
            except Exception as e:
                print('RECEIVE', e)
                exit(1)
    
    def write(self):
        while (True):
            try:
                time.sleep(1)
                message = input(f'{self.text}\n >')
                self.client.send(message.encode("utf-8"))
            except Exception as e:
                print('WRITE', e)
                exit(1)

    def start(self):
        self.receive_thread.start()
        self.write_thread.start()
        exit(1)