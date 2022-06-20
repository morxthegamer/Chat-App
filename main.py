from tkinter import *
from app import login, sign_up
from threading import Thread

def start():
    window = Tk()
    window.geometry('400x400')
    window.config(bg='black')
    window.title('Cord Chat App')

    def log():
        window.destroy()
        login()

    def sign():
        window.destroy()
        sign_up()
    
    chat_label = Label(
        window,
        text="Cord Chat",
        font=("Courier", 20, 'bold'),
        bg='black',
        fg='white'
    )

    sign_up_button = Button(
        window,
        text="Sign Up",
        font=("Courier", 14, "bold"),
        bg='white',
        fg='black',
        command=sign
    )

    login_button = Button(
        window,
        text="Log In",
        font=("Courier", 14, "bold"),
        bg='black',
        fg='white',
        command=log
    )

    chat_label.place(x=130, y=60)
    sign_up_button.place(x=116, y=130)
    login_button.place(x=210, y=130)

    window.mainloop()

if __name__ == "__main__":
    working_thread = Thread(target=start)
    working_thread.start()