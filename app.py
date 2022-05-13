from client import Client
import os

class App:
    def __init__(self):
      self.host = '127.0.0.1'
      self.port = 9000
      self.client = Client(self.host, self.port)

    def login(self):
        os.system("clear")
        username = input("Please enter your username: ")
        password = input("Please enter you password: ")

        information = self.user_data.getDataJson(f"user[{username}].json")

        if (information["Username"] != username):
            print("Login failed. Wrong Username. Please try again.")
            exit(1)

        if (information["Password"] != password):
            print("Login failed. Wrong Password. Please try again.")
            exit(1)

        if (information["Username"] == username and information["Password"] == password):
            print("Successfully logged in!")
            
        return information

    def start(self):
      self.client.start()