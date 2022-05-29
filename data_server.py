import threading, socket, os
from data import Data

HOST = '127.0.0.1'
PORT = 9000

class DataServer:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        self.data = Data('DataBase')
        self.clients = []
        self.users = {}

    def handle_client_login(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'LOGIN REQUEST'):
                    username = client.recv(1024).decode('utf-8')
                    password = client.recv(1024).decode('utf-8')

                    try:
                        user = self.data.getDataJson(f'user[{username}].json')
                        self.users[client]
                    except Exception:
                        client.send(f'Login Failed. No username such as {username} exists.'.encode('utf-8'))
                    
                    if (user['Password'] != password):
                        client.send('Login Failed. Wrong Password.'.encode('utf-8'))

                    if (user['Username'] == username and user['Password'] == password):
                        client.send('Successfully logged in!'.encode('utf-8'))

                    self.clients.remove(client)
                    client.close()

            except Exception:
                client.send('An error occured.'.encode('utf-8'))
                self.clients.remove(client)
                client.close()

    def handle_client_sign_up(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'SIGN UP REQUEST'):
                    username = client.recv(1024).decode('utf-8')
                    email = client.recv(1024).decode('utf-8')
                    password = client.recv(1024).decode('utf-8')
                    age = client.recv(1024).decode('utf-8')
                    phone = client.recv(1024).decode('utf-8')

                    for file in os.listdir('DataBase'):
                        filename = file[5:-6]

                        if username == filename:
                            client.send('This username is already taken. Please try again.'.encode('utf-8'))

                        mail = self.data.getDataJson(file)['Email']

                        if (email == mail):
                            client.send('This email is already taken. Please try again.'.encode('utf-8'))

                    user = {
                        'Username': username,
                        'Email': email,
                        'Password': password,
                        'Age': age,
                        'Contact': phone,
                        'Extras': {
                            'Theme': 'white',
                            'Badge': '💬',
                            'Text': 'Type A Message: ',
                            'Boost Subscription': False
                        }
                    }

                    self.data.setDataJson(f'user[{username}].json', user)
                    client.send('Successfully signed up!'.encode('utf-8'))

                    self.clients.remove(client)
                    client.close()

            except Exception:
                client.send('An error occured.'.encode('utf-8'))
                self.clients.remove(client)
                client.close()

    def handle_client_settings(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'SETTINGS REQUEST'):
                    pass

            except Exception:
                pass

    def handle_account_deletion(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'DELETE ACCOUNT REQUEST'):
                    client.send('Are you sure you want to delete your account?'.encode('utf-8'))
                    os.remove("DataBase/user[{}].json".format(self.users[self.clients.index(client)]["Username"]))
                    

            except Exception:
                pass

    def handle_information(self, client):
        while True:
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'INFO REQUEST'):
                    client.send(str(self.users[self.clients.index(client)]).encode('utf-8'))

            except Exception:
                pass

    def receive(self):
        client, address = self.server.accept()
        print(f'{client} connected with address: {address}.')

        self.clients.append(client)

        login_thread = threading.Thread(target=self.handle_client_login, args=(client,))
        sign_up_thread = threading.Thread(target=self.handle_client_sign_up, args=(client,))
        settings_thread = threading.Thread(target=self.handle_client_settings, args=(client,))
        del_acc_thread = threading.Thread(target=self.handle_account_deletion, args=(client,))
        handle_info_thread = threading.Thread(target=self.handle_information, args=(client,))
        
        login_thread.start()
        sign_up_thread.start()
        settings_thread.start()
        del_acc_thread.start()
        handle_info_thread.start()

    def start(self):
        print(f'Server listening on {HOST}...')
        self.receive()

if __name__ == '__main__':
    server = DataServer(HOST, PORT)
    server.start()