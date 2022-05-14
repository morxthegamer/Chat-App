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
            bg='black',
            fg='white',
            command=self.app.sign_up
        )

        self.login_button = Button(
            self.window,
            text="Log In",
            font=("Courier", 14, "bold"),
            bg='black',
            fg='white',
            command=self.app.login
        )

        self.status_button = Button(
            self.window,
            text="Status",
            font=("Courier", 14, "bold"),
            bg='black',
            fg='white',
            command=self.app.status
        )

        self.delete_button = Button(
            self.window,
            text="Delete Account",
            font=("Courier", 14, "bold"),
            bg='black',
            fg='white',
            command=self.app.delete_account
        )

        self.change_button = Button(
            self.window,
            text="Configure",
            font=("Courier", 14, "bold"),
            bg='black',
            fg='white',
            command=self.app.change
        )

    def start(self):
        self.chat_label.place(x=90, y=60)
        self.sign_up_button.place(x=150, y=150)
        self.login_button.place(x=155, y=190)
        self.status_button.place(x=155, y=230)
        self.change_button.place(x=140, y=270)
        self.delete_button.place(x=115, y=310)

        self.window.mainloop()

if __name__ == "__main__":
    app = Main()
    app.start()