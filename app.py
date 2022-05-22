from client import Client
from data import Data
import os, time
from tkinter import *

class App:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9000
        self.data = Data('DataBase')

    def status(self):
        self.status_wind = Tk()
        self.status_wind.geometry('400x400')

        self.status_lbl = Label(
            self.status_wind,
            text='Status',
            font=('Times', 20, 'bold')
        )

        i = self.login()
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

    def login(self):            
        self.login_wind = Tk()
        self.login_wind.geometry('400x400')
        self.login_wind.config(bg='black')

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

        self.confirm_button = Button(
            self.login_wind,
            text='Enter',
            font=('Courier', 12, 'bold'),
            bg='black',
            fg='white'
            command=get_info
        )
        
        self.login_label.place(x=100, y=60)
        self.name_label.place(x=65, y=140)
        self.pass_label.place(x=65, y=160)
        self.username.place(x=145, y=140)
        self.password.place(x=145, y=160)
        self.confirm_button.place(x=165, y=200)

        name, pw = self.username.get('1.0', 'end'), self.password.get()

        def get_info(self):
            print('Logging in...\n')
            time.sleep(2)

            i = self.data.getDataJson(f"user[{self.username.get('1.0', 'end')}].json")

            if (i["Username"] != name):
                print("Login failed. Wrong Username. Please try again.")
                exit(1)

            if (i["Password"] != pw):
                print("Login failed. Wrong Password. Please try again.")
                exit(1)

            if (i["Username"] == name and i["Password"] == pw):
                print("Successfully logged in!")
                
            return i

        self.login_wind.mainloop()

    def sign_up(self):
        os.system('cls')
        username = input("Please enter your username: ")
        email = input("Please enter your email: ")
        password = input("Please enter you password: ")

        for file in os.listdir('DataBase'):
            filename = file[5:-6]

            if username == filename:
                print('This username is already taken. Please try again.')
                exit(1)

            mail = self.data.getDataJson(file)['Email']

            if (email == mail):
                print('This email is already taken. Please try again.')
                exit(1)

        os.system('cls')
        age = input('Please enter your age: ')
        phone_number = input('Please enter your phone number: ')

        user = {
            'Username': username,
            'Email': email,
            'Password': password,
            'Age': age,
            'Contact': phone_number,
            'Extras': {
                'Theme': 'white',
                'Badge': '💬',
                'Text': 'Type A Message: ',
                'Boost Subscription': False
            }
        }

        print('Signing you up...')
        time.sleep(2)

        self.data.setDataJson(f'user[{username}].json', user)
        print(f"Sign up was successful! Welcome {username}.")

    def delete_account(self):
        os.system("cls")
        i = self.login()

        confirmation = input('Are you sure you want to delete your account? (y/n): ')

        if confirmation == 'y':
            reason = input("Please tells us why:\n> ")
            os.remove("DataBase/user[{}].json".format(i["Username"]))
            print(f"Account successfully deleted. With reason:\n\n{reason}.")

    def change(self):
        i = self.login()
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

    

    def start(self):
        i = self.login()
        self.client = Client(self.host, self.port, i["Username"], i['Extras']['Theme'], i['Extras']['Badge'], i['Extras']['Text'])
        self.client.start()