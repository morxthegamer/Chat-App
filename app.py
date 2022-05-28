from client import Client
from data import Data
import os, time, threading
from tkinter import *

class App:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9000
        self.data = Data('DataBase')

    def status(self):
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

    def delete_account(self):
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
        self.client = Client(self.host, self.port, i["Username"], i['Extras']['Theme'], i['Extras']['Badge'], i['Extras']['Text'])
        self.client.start()