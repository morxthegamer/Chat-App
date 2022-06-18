from chat_client import Client
from data import Data
from boost import Boost
import os, time, threading, socket, json
from tkinter import *

HOST, PORT = '127.0.0.1', 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def status():
    client.send('INFO REQUEST'.encode('utf-8'))
    i = eval(client.recv(1024).decode('utf-8'))

    status_wind = Tk()
    status_wind.geometry('400x400')
    status_wind.config(bg='black')
    status_wind.title('Status')

    status_lbl = Label(
        status_wind,
        text='Status',
        font=('Times', 20, 'bold'),
        bg='black',
        fg='white'
    )

    status_text = Label(
        status_wind,
        text=f"""
    Username: {i['Username']}
    Email: {i['Email']}
    Password: {i['Password']}
    Age: {i['Age']}
    Phone: {i['Contact']}

    Current Badge: {i['Extras']['Badge']}
    Current Theme: {i['Extras']['Theme']}
    Frontline Text: {i['Extras']['Text']}
    Boost Subscription: {i['Extras']['Boost Subscription']}
    """,
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    status_lbl.place(x=169, y=60)
    status_text.place(x=0, y=100)

    status_wind.mainloop()

def delete_account():
    del_acc_wind = Tk()
    del_acc_wind.geometry('400x400')
    del_acc_wind.config(bg='black')
    del_acc_wind.title('Delete Your Account')

    confirmation = Label(
        del_acc_wind,
        text='''
         Are you sure you want 
        to delete your account?
        ''',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    def send_info():
        client.send('DELETE ACCOUNT REQUEST')
        done = client.recv(1024).decode('utf-8')
        print(done)
        exit(0)

    yes_button = Button(
        del_acc_wind,
        text='Yes',
        font=('Courier', 12, 'bold'),
        bg='green',
        fg='black',
        command=send_info
    )

    no_button = Button(
        del_acc_wind,
        text='No',
        font=('Courier', 12, 'bold'),
        bg='red',
        fg='black',
        command=del_acc_wind.destroy
    )

    confirmation.place(x=0, y=90)
    yes_button.place(x=150, y=150)
    no_button.place(x=200, y=150)
    del_acc_wind.mainloop()

def settings():
    settings_wind = Tk()
    settings_wind.geometry('400x400')
    settings_wind.config(bg='black')
    settings_wind.title('Settings')

    settings_lbl = Label(
        settings_wind,
        text='Settings',
        font=('Times', 20, 'bold')
    )

    items = ['Password', 'Age', 'Contact']
    item = StringVar()
    item.set(items[0])

    options = OptionMenu(
        settings_wind,
        item,
        *items
    )
    
    adj_lbl = Label(
        settings_wind,
        text='What would you like to change?',
        font=('Courier', 12, 'bold'),
        bg='black',
        fg='white'
    )

    adjustment = Entry(
        settings_wind,
        textvariable=adj_lbl,
        width=30
    )

    adj_button = Button(
        settings_wind,
        text='Change',
        font=('Courier', 12, 'bold'),
        bg='white',
        fg='green'
    )

    def send_info():
        pass

def start():
    client.send('INFO REQUEST'.encode('utf-8'))
    host, port = '127.0.0.1', 9000
    info = json.loads(client.recv(1024).decode('utf-8'))

    chatClient = Client(host, port, info["Username"], info['Extras']['Theme'], info['Extras']['Badge'], info['Extras']['Text'])
    chatClient.start()

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
        command=status
    )

    delete_button = Button(
        window,
        text="Delete Account",
        font=("Courier", 14, "bold"),
        bg='green',
        fg='white',
        command=delete_account
    )

    change_button = Button(
        window,
        text="Settings",
        font=("Courier", 14, "bold"),
        bg='gray',
        fg='black',
        command=settings
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
        command=start
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
        client.send(username.get().encode('utf-8'))
        client.send(email.get().encode('utf-8'))
        client.send(password.get().encode('utf-8'))
        client.send(age.get().encode('utf-8'))
        client.send(phone_number.get().encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(response)

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