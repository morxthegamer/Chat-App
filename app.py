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
        i = self.login()

        status_wind = Tk()
        status_wind.geometry('400x400')
        status_wind.config(bg='black')
        status_wind.title('Status')

        status_lbl = Label(
            status_wind,
            text='Status',
            font=('Times', 20, 'bold')
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
            font=('Courier', 20, 'bold')
        )

        status_lbl.place(x=110, y=160)
        status_text.place(x=110, y=200)

        status_wind.mainloop()

    def login(self):            
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
            name, pw = username.get(), password.get()
            login_wind.destroy()
            
            print('Logging in...\n')
            time.sleep(2)

            i = self.data.getDataJson(f"user[{name}].json")

            if (i["Username"] != name):
                print("Login failed. Wrong Username. Please try again.")
                exit(1)

            if (i["Password"] != pw):
                print("Login failed. Wrong Password. Please try again.")
                exit(1)

            if (i["Username"] == name and i["Password"] == pw):
                print("Successfully logged in!")
                
            return i

        confirm_button = Button(
            login_wind,
            text='Enter',
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
        confirm_button.place(x=165, y=200)

        login_wind.mainloop()

    def sign_up(self):
        sign_up_wind = Tk()
        sign_up_wind.geometry('400x400')
        sign_up_wind.config(bg='black')
        sign_up_wind.title('Sign Up')

        # Labels

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

        # Text Area

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

        def set_data():
            name, mail, pw, age, number = username.get(), email.get(), password.get(), age.get(), phone_number.get()
            for file in os.listdir('DataBase'):
                filename = file[5:-6]

                if name == filename:
                    print('This username is already taken. Please try again.')
                    exit(1)

                mail = self.data.getDataJson(file)['Email']

                if (email == mail):
                    print('This email is already taken. Please try again.')
                    exit(1)

            user = {
                'Username': name,
                'Email': mail,
                'Password': pw,
                'Age': age,
                'Contact': number,
                'Extras': {
                    'Theme': 'white',
                    'Badge': '💬',
                    'Text': 'Type A Message: ',
                    'Boost Subscription': False
                }
            }

            print('Signing you up...')
            time.sleep(2)

            self.data.setDataJson(f'user[{name}].json', user)
            print(f"Sign up was successful! Welcome {name}.")

        confirm_button = Button(
            sign_up_wind,
            text='Enter',
            font=('Courier', 12, 'bold'),
            bg='black',
            fg='white',
            command=set_data
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
        confirm_button.place(x=165, y=280)

        sign_up_wind.mainloop()

    def delete_account(self):
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