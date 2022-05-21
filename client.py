import socket, threading, time
from data import Data
from termcolor import cprint
from tkinter import *
from tkinter import scrolledtext

class Client:
    def __init__(self, host, port, nickname, theme, badge, text):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = nickname
        self.theme = theme
        self.badge = badge
        self.text = text
      
        self.receive_thread = threading.Thread(target=self.receive)
        self.write_thread = threading.Thread(target=self.write_text)

    def calc_space(self, text_length):
        space = 174

        for i in range(text_length):
            space -= 5

        return space

    def write_text(self):
        self.message_wind = Tk()
        self.message_wind.geometry('400x400')
        self.message_wind.config(bg='black')
        self.message_wind.title('Chat')

        self.message_label = Label(
            self.message_wind,
            text=self.nickname,
            font=("Courier", 20, 'bold'),
            bg='black',
            fg=self.theme
        )

        self.message_bar = scrolledtext.ScrolledText(
            self.message_wind,
            wrap=WORD,
            width=50,
            height=2,
            font=("Courier", 15, 'bold'),
            fg=self.theme,
            bg='black'
        )

        self.message_button = Button(
            self.message_wind,
            text='Send',
            font=('Courier', 15, 'bold'),
            bg='black',
            fg=self.theme,
            command=self.write
        )

        self.message_bar.insert('1.0', self.text)

        self.message_label.place(x=self.calc_space(len(self.nickname)), y=40)
        self.message_bar.place(x=1, y=100)
        self.message_button.place(x=160, y=170)
        self.message_wind.mainloop()
  
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
        try:
            message = self.message_bar.get('1.0', 'end')
            self.client.send(message.encode('utf-8'))
        except Exception as e:
            print('WRITE', e)
            exit(1)

    def start(self):
        self.receive_thread.start()
        self.write_thread.start()
        exit(1)