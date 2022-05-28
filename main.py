from app import App
from tkinter import *
from threading import Thread

class Main:
    def __init__(self):
        self.app = App()
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

        self.slang_line_label = Label(
            self.window,
            text="Where Communication happens best!",
            font=("Courier", 10, "bold"),
            bg='black',
            fg='white',
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
            text="Delete Account",
            font=("Courier", 14, "bold"),
            bg='green',
            fg='white',
            command=self.app.delete_account
        )

        self.change_button = Button(
            self.window,
            text="Settings",
            font=("Courier", 14, "bold"),
            bg='gray',
            fg='black',
            command=self.app.change
        )

        self.boost_button = Button(
            self.window,
            text="Boost Subscription",
            font=("Courier", 14, "bold"),
            bg='purple',
            fg='white',
            command=self.app.change
        )

        self.start_button = Button(
            self.window,
            text="Join To Chat",
            font=("Courier", 14, "bold"),
            bg='blue',
            fg='white',
            command=self.start_to_chat
        )

    def start_to_chat(self):
        self.window.destroy()
        self.app.start()

    def start(self):
        self.chat_label.place(x=135, y=60)
        self.slang_line_label.place(x=73, y=110)
        self.status_button.place(x=74, y=180)
        self.change_button.place(x=74, y=219)
        self.delete_button.place(x=157, y=180)
        self.boost_button.place(x=95, y=258)
        self.start_button.place(x=179, y=219)

        self.window.mainloop()

if __name__ == "__main__":
    app = Main()
    app.start()