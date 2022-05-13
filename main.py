from app import App
from tkinter import *

class Main:
    def __init__(self):
        self.app = App()
        self.window = Tk()
        self.window.geometry('400x400')
        self.window.config(bg='black')
        self.window.title('Chat App')

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
        self.window.mainloop()

    

if __name__ == "__main__":
    main()