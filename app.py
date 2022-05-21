from client import Client
from data import Data
import os, time

class App:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 9000
        self.data = Data('DataBase')

    def status(self):
        i = self.login()
        print(
            f"""
            Username: {i['Username']}
            Email: {i['Email']}
            Password: {i['Password']}
            Age: {i['Age']}
            Phone: {i['Contact']}
            Current Badge: {i['Badge']}
            Current Theme: {i['Theme']}
            Frontline Text: {i['Text']}
        """)

    def login(self):
        os.system("cls")
        print('Please Login.\n')
        username = input("Please enter your username: ")
        password = input("Please enter you password: ")

        os.system('cls')
        print('Logging in...\n')
        time.sleep(2)

        i = self.data.getDataJson(f"user[{username}].json")

        if (i["Username"] != username):
            print("Login failed. Wrong Username. Please try again.")
            exit(1)

        if (i["Password"] != password):
            print("Login failed. Wrong Password. Please try again.")
            exit(1)

        if (i["Username"] == username and i["Password"] == password):
            print("Successfully logged in!")
            
        return i

    def sign_up(self):
        os.system('cls')
        username = input("Please enter your username: ")
        email = input("Please enter your email: ")
        password = input("Please enter you password: ")

        os.system('cls')
        age = input('Please enter your age: ')
        phone_number = input('Please enter your phone number: ')

        user = {
            'Username': username,
            'Email': email,
            'Password': password,
            'Age': age,
            'Contact': phone_number,
            'Theme': 'white',
            'Badge': '💬',
            'Text': 'Type A Message: '
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
        self.client = Client(self.host, self.port, i["Username"], i['Theme'], i['Badge'], i['Text'])
        self.client.start()