from tkinter import *
from app import *
from threading import Thread

class Start:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.config(bg='black')
        self.window.title('Cord Chat App')
        
        self.chat_label = Label(
            self.window,
            text="Cord Chat",
            font=("Courier", 20, 'bold'),
            bg='black',
            fg='white'
        )

        self.sign_up_button = Button(
            self.window,
            text="Sign Up",
            font=("Courier", 14, "bold"),
            bg='white',
            fg='black',
            command=self.sign
        )

        self.login_button = Button(
            self.window,
            text="Log In",
            font=("Courier", 14, "bold"),
            bg='black',
            fg='white',
            command=self.log
        )

        self.chat_label.place(x=130, y=60)
        self.sign_up_button.place(x=116, y=130)
        self.login_button.place(x=210, y=130)

        self.window.mainloop()

    def log(self):
        self.window.destroy()
        login()

    def sign(self):
        self.window.destroy()
        sign_up()

if __name__ == "__main__":
    app = Start()