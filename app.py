import os, time, threading, socket, json
from tkinter import *
from options import status, delete_account, settings, start
from gui import SuccessWindow, ErrorWindow

HOST, PORT = '127.0.0.1', 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def startup():
    window = Tk()
    window.geometry('400x400')
    window.config(bg='black')
    window.title('Cord Chat App')
    
    chat_label = Label(
        window,
        text="Cord Chat",
        font=("Courier", 20, 'bold'),
        bg='black',
        fg='white'
    )

    slang_line_label = Label(
        window,
        text="Where Communication happens best!",
        font=("Courier", 10, "bold"),
        bg='black',
        fg='white',
    )

    status_button = Button(
        window,
        text="Status",
        font=("Courier", 14, "bold"),
        bg='yellow',
        fg='black',
        command=lambda: status(client)
    )

    delete_button = Button(
        window,
        text="Delete Account",
        font=("Courier", 14, "bold"),
        bg='green',
        fg='white',
        command=lambda: delete_account(client)
    )

    change_button = Button(
        window,
        text="Settings",
        font=("Courier", 14, "bold"),
        bg='gray',
        fg='black',
        command=lambda: settings(client)
    )

    boost_button = Button(
        window,
        text="Boost Subscription",
        font=("Courier", 14, "bold"),
        bg='purple',
        fg='white'
    )

    start_button = Button(
        window,
        text="Join To Chat",
        font=("Courier", 14, "bold"),
        bg='blue',
        fg='white',
        command=lambda: start(client)
    )
    
    chat_label.place(x=135, y=60)
    slang_line_label.place(x=73, y=110)
    status_button.place(x=74, y=180)
    change_button.place(x=74, y=219)
    delete_button.place(x=157, y=180)
    boost_button.place(x=95, y=258)
    start_button.place(x=179, y=219)

    window.mainloop()

def login():
    login_wind = Tk()
    login_wind.geometry('400x400')
    login_wind.config(bg='black')
    login_wind.title('Log In')

    login_label = Label(
        login_wind,
        text='Please Login',
        font=('Courier', 20,'bold'),
        bg='black',
        fg='white'
    )

    name_label = Label(
        login_wind,
        text='Username:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    pass_label = Label(
        login_wind,
        text='Password:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    username = Entry(
        login_wind,
        textvariable=name_label,
        width=30,
    )

    password = Entry(
        login_wind,
        textvariable=pass_label,
        width=30,
    )

    def get_info():
        client.send('LOGIN REQUEST'.encode('utf-8'))
        print(username.get(), password.get())
        
        client.send(username.get().encode('utf-8'))
        client.send(password.get().encode('utf-8'))
        login_wind.destroy()

        data = client.recv(1024).decode('utf-8')
        print(data)

        if ('Failed' in data):
            e = ErrorWindow()
            exit(1)
            
        if ('Success' in data):
            s = SuccessWindow()
            startup()

    login_button = Button(
        login_wind,
        text='Log In',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white',
        command=get_info
    )
    
    login_label.place(x=100, y=60)
    name_label.place(x=65, y=140)
    pass_label.place(x=65, y=160)
    username.place(x=145, y=140)
    password.place(x=145, y=160)
    login_button.place(x=165, y=280)

    login_wind.mainloop()

def sign_up():
    sign_up_wind = Tk()
    sign_up_wind.geometry('400x400')
    sign_up_wind.config(bg='black')
    sign_up_wind.title('Sign Up')

    # Info Labels

    sign_up_lbl = Label(
        sign_up_wind,
        text='Sign Up',
        font=('Courier', 20, 'bold'),
        bg='black',
        fg='white'
    )

    name_label = Label(
        sign_up_wind,
        text='Username:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    mail_label = Label(
        sign_up_wind,
        text='Email:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    pass_label = Label(
        sign_up_wind,
        text='Password:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    age_label = Label(
        sign_up_wind,
        text='Age:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    phone_number_label = Label(
        sign_up_wind,
        text='Phone Number:',
        font=('Courier', 10, 'bold'),
        bg='black',
        fg='white'
    )

    # Text Fields

    username = Entry(
        sign_up_wind,
        textvariable=name_label,
        width=30,
    )

    email = Entry(
        sign_up_wind,
        textvariable=mail_label,
        width=30,
    )

    password = Entry(
        sign_up_wind,
        textvariable=pass_label,
        width=30,
    )

    age = Entry(
        sign_up_wind,
        textvariable=age_label,
        width=30,
    )

    phone_number = Entry(
        sign_up_wind,
        textvariable=phone_number_label,
        width=30,
    )

    def create_account():
        client.send('SIGN UP REQUEST'.encode('utf-8'))

        client.send(username.get().encode('utf-8'))
        time.sleep(1)

        client.send(email.get().encode('utf-8'))
        time.sleep(1)

        client.send(password.get().encode('utf-8'))
        time.sleep(1)

        client.send(age.get().encode('utf-8'))
        time.sleep(1)

        client.send(phone_number.get().encode('utf-8'))
        sign_up_wind.destroy()

        response = client.recv(1024).decode('utf-8')

        if 'Please' in response:
            print(response)
            e = ErrorWindow
            exit(1)

        if 'Success' in response:
            print(response)
            s = SuccessWindow()

    sign_up_button = Button(
        sign_up_wind,
        text='Sign Up',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white',
        command=create_account
    )

    sign_up_lbl.place(x=143, y=60)
    name_label.place(x=65, y=140)
    mail_label.place(x=89, y=160)
    pass_label.place(x=65, y=180)
    age_label.place(x=105, y=200)
    phone_number_label.place(x=33, y=220)

    username.place(x=145, y=140)
    email.place(x=145, y=160)
    password.place(x=145, y=180)
    age.place(x=145, y=200)
    phone_number.place(x=145, y=220)
    sign_up_button.place(x=165, y=280)

    sign_up_wind.mainloop()