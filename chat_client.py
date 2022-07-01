import socket, threading, time
from tkinter import messagebox
from data import Data
from termcolor import cprint
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class Client:
    def __init__(self, host, port, nickname, theme, badge, text):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.nickname = nickname
        self.theme, self.badge, self.text = theme, badge, text
        self.server = f'{host}:{port} | Cord Chat'

        self.message_wind = Tk()
        self.message_wind.geometry('400x600')
        self.message_wind.config(bg='black')
        self.message_wind.title('Chat')

        self.message_label = Label(
            self.message_wind,
            text=self.server,
            font=("Courier", 22, 'bold'),
            bg='black',
            fg=self.theme
        )

        self.messages = ScrolledText(
            self.message_wind,
            wrap=WORD,
            width=30,
            height=15,
            font=("Courier", 15, 'bold'),
            fg=self.theme,
            bg='black',
            state=DISABLED
        )

        self.send_messages = Label(
            self.message_wind,
            text=self.text,
            font=('Times', 14, 'bold'),
            bg='black',
            fg=self.theme
        )

        self.message = Text(
            self.message_wind,
            font=("Courier", 15, 'bold'),
            width=30,
            height=1.5,
            bg='black',
            fg=self.theme
        )

        self.message_button = Button(
            self.message_wind,
            text='Send',
            font=('Courier', 15, 'bold'),
            bg='black',
            fg=self.theme,
            command=self.write,
            width=10
        )

        self.message_label.pack()
        self.messages.pack()
        self.send_messages.pack()
        self.message.pack()
        self.message_button.place(x=136, y=472.5)

        self.message_wind.mainloop()
      
        self.receive_thread = threading.Thread(target=self.receive)
        self.gui_thread = threading.Thread(target=self.start_gui)

    def start_gui(self):
        self.window.mainloop()
  
    def receive(self):
        while (True):
            try:
                message = self.client.recv(1024).decode("utf-8")

                if message == "NICKNAME REQUEST":
                    self.client.send(self.nickname.encode('utf-8'))
                elif message == 'BADGE REQUEST':
                    self.client.send(self.badge.encode('utf-8'))
                else:
                    self.messages['state'] = NORMAL
                    self.messages.insert('end', message)
                    self.messages['state'] = DISABLED

            except Exception as e:
                print('RECEIVE', e)
                exit(1)
  
    def write(self):
        try:
            message = self.message.get('1.0', 'end')
            self.client.send(message.encode('utf-8'))
        except Exception as e:
            print('WRITE', e)
            exit(1)

    def start(self):
        self.receive_thread.start()
        self.gui_thread.start()
        exit(1)