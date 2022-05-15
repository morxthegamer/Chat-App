from app import App
from tkinter import *
from threading import Thread

class Main:
    def __init__(self):
        self.app = App()
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.config(bg='black')
        self.window.title('Chat App')
        
        self.chat_label = Label(
            self.window,
            text="Welcome to Chat App!",
            font=("Courier", 14, 'bold'),
            bg='black',
            fg='white'
        )

        self.sign_up_button = Button(
            self.window,
            text="Sign Up",
            font=("Courier", 14, "bold"),
            bg='white',
            fg='black',
            command=self.app.sign_up
        )

        self.status_button = Button(
            self.window,
            text="Status",
            font=("Courier", 14, "bold"),
            bg='yellow',
            fg='black',
            command=self.app.status
        )

        self.delete_button = Button(
            self.window,
            text="Del Acc",
            font=("Courier", 14, "bold"),
            bg='green',
            fg='black',
            command=self.app.delete_account
        )

        self.change_button = Button(
            self.window,
            text="Configure",
            font=("Courier", 14, "bold"),
            bg='blue',
            fg='white',
            command=self.app.change
        )

        self.start_button = Button(
            self.window,
            text="Chat",
            font=("Courier", 14, "bold"),
            bg='purple',
            fg='white',
            command=self.app.start
        )

    def start(self):
        self.chat_label.place(x=90, y=60)
        self.sign_up_button.place(x=150, y=120)
        self.status_button.place(x=113, y=200)
        self.change_button.place(x=113, y=239)
        self.delete_button.place(x=196, y=200)
        self.start_button.place(x=229, y=239)

        self.window.mainloop()

if __name__ == "__main__":
    app = Main()
    app.start()