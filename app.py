from chat_client import Client
from data import Data
import os, time, threading, socket, json
from tkinter import *

HOST, PORT = '127.0.0.1', 8000

app_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
app_client.connect((HOST, PORT))

class Start:
    def __init__(self):
        app_client.send('INFO REQUEST')
        self.host, self.port = '127.0.0.1', 9000
        self.info = json.loads(app_client.recv(1024).decode('utf-8'))

        self.client = Client(self.host, self.port, self.info["Username"], self.info['Extras']['Theme'], self.info['Extras']['Badge'], self.info['Extras']['Text'])
        self.client.start()

class Status:
    def __init__(self):
        app_client.send('INFO REQUEST')
        i = json.loads(app_client.recv(1024).decode('utf-8'))

        self.status_wind = Tk()
        self.status_wind.geometry('400x400')
        self.status_wind.config(bg='black')
        self.status_wind.title('Status')

        self.status_lbl = Label(
            self.status_wind,
            text='Status',
            font=('Times', 20, 'bold')
        )

        self.status_text = Label(
            self.status_wind,
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
            font=('Courier', 20, 'bold')
        )

        self.status_lbl.place(x=110, y=160)
        self.status_text.place(x=110, y=200)

        self.status_wind.mainloop()

class DeleteAccount:
    pass

class Settings:
    def __init__(self):
        pass

    def change(self):
        item = input('What do you want to change?: ')
        if (item == 'Username' or item == 'Email' or item == 'Badge' or item == 'Theme' or item == 'Text'):
            print(f'You cannot change your {item}.')
            exit(1)

        adjustment = input(f'Ok, Please enter your new {item}: ')

        print('Saving...')
        i[f'{item}'] = adjustment
        self.data.setDataJson('user[{}].json'.format(i['Username']), i)
        time.sleep(2)

        print('Your changes have been saved!')
    
class LoginWindow:
    def __init__(self):
        self.login_wind = Tk()
        self.login_wind.geometry('400x400')
        self.login_wind.config(bg='black')
        self.login_wind.title('Log In')

        self.login_label = Label(
            self.login_wind,
            text='Please Login',
            font=('Courier', 20,'bold'),
            bg='black',
            fg='white'
        )

        self.name_label = Label(
            self.login_wind,
            text='Username:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        self.pass_label = Label(
            self.login_wind,
            text='Password:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        self.username = Entry(
            self.login_wind,
            textvariable=self.name_label,
            width=30,
        )

        self.password = Entry(
            self.login_wind,
            textvariable=self.pass_label,
            width=30,
        )

        self.login_button = Button(
            self.login_wind,
            text='Log In',
            font=('Courier', 12, 'bold'),
            bg='black',
            fg='white',
            command=
        )
        
        self.login_label.place(x=100, y=60)
        self.name_label.place(x=65, y=140)
        self.pass_label.place(x=65, y=160)
        self.username.place(x=145, y=140)
        self.password.place(x=145, y=160)
        self.login_button.place(x=165, y=280)

        self.login_wind.mainloop()

    def get_info(self):
        app_client.send('LOGIN REQUEST'.encode('utf-8'))
        app_client.send(self.username.get().encode('utf-8'))
        app_client.send(self.password.get().encode('utf-8'))

        data = json.loads(app_client.recv(1024).decode('utf-8'))
        print(data)
        
class SignUpWindow:
    def __init__(self):
        self.sign_up_wind = Tk()
        self.sign_up_wind.geometry('400x400')
        self.sign_up_wind.config(bg='black')
        self.sign_up_wind.title('Sign Up')

        # Info Labels

        self.sign_up_lbl = Label(
            self.sign_up_wind,
            text='Sign Up',
            font=('Courier', 20, 'bold'),
            bg='black',
            fg='white'
        )

        self.name_label = Label(
            self.sign_up_wind,
            text='Username:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        self.mail_label = Label(
            self.sign_up_wind,
            text='Email:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        self.pass_label = Label(
            self.sign_up_wind,
            text='Password:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        self.age_label = Label(
            self.sign_up_wind,
            text='Age:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        self.phone_number_label = Label(
            self.sign_up_wind,
            text='Phone Number:',
            font=('Courier', 10, 'bold'),
            bg='black',
            fg='white'
        )

        # Text Fields

        self.username = Entry(
            self.sign_up_wind,
            textvariable=self.name_label,
            width=30,
        )

        self.email = Entry(
            self.sign_up_wind,
            textvariable=self.mail_label,
            width=30,
        )

        self.password = Entry(
            self.sign_up_wind,
            textvariable=self.pass_label,
            width=30,
        )

        self.age = Entry(
            self.sign_up_wind,
            textvariable=self.age_label,
            width=30,
        )

        self.phone_number = Entry(
            self.sign_up_wind,
            textvariable=self.phone_number_label,
            width=30,
        )

        self.sign_up_button = Button(
            self.sign_up_wind,
            text='Sign Up',
            font=('Courier', 12, 'bold'),
            bg='black',
            fg='white',
            command=self.create_account
        )

        self.sign_up_lbl.place(x=143, y=60)
        self.name_label.place(x=65, y=140)
        self.mail_label.place(x=89, y=160)
        self.pass_label.place(x=65, y=180)
        self.age_label.place(x=105, y=200)
        self.phone_number_label.place(x=33, y=220)

        self.username.place(x=145, y=140)
        self.email.place(x=145, y=160)
        self.password.place(x=145, y=180)
        self.age.place(x=145, y=200)
        self.phone_number.place(x=145, y=220)
        self.sign_up_button.place(x=165, y=280)

        self.sign_up_wind.mainloop()

    def create_account(self):
        app_client.send(self.username.get().encode('utf-8'))
        app_client.send(self.email.get().encode('utf-8'))
        app_client.send(self.password.get().encode('utf-8'))
        app_client.send(self.age.get().encode('utf-8'))
        app_client.send(self.phone_number.get().encode('utf-8'))

        response = app_client.recv(1024).decode('utf-8')
        print(response)