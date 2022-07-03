import threading, socket, os
from data import Data

HOST = '127.0.0.1'
PORT = 8000

class DataServer:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        self.data = Data('DataBase')
        self.clients = []
        self.users = []

    def handle_client(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')
                print(request)

                # LOGIN
                if (request == 'LOGIN REQUEST'):
                    try:
                        username = client.recv(1024).decode('utf-8')
                        password = client.recv(1024).decode('utf-8')

                        print(username, password)

                        try:
                            user = self.data.getDataJson(f'user[{username}].json')
                            self.users.insert(self.clients.index(client), user)

                        except Exception:
                            client.send(f'Login Failed. No username such as {username} exists.'.encode('utf-8'))
                        
                        if (user['Password'] != password):
                            client.send('Login Failed. Wrong Password.'.encode('utf-8'))

                        if (user['Username'] == username and user['Password'] == password):
                            client.send('Successfully logged in!'.encode('utf-8'))

                    except Exception as e:
                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                # SIGN UP
                if (request == 'SIGN UP REQUEST'):
                    try:
                        username = client.recv(1024).decode('utf-8')
                        email = client.recv(1024).decode('utf-8')
                        password = client.recv(1024).decode('utf-8')
                        age = client.recv(1024).decode('utf-8')
                        phone = client.recv(1024).decode('utf-8')

                        print(username, email, password, age, phone)

                        for file in os.listdir('DataBase'):
                            filename = file[5:-6]
                            print(file)

                            if username == filename:
                                client.send('This username is already taken. Please try again.'.encode('utf-8'))
                                self.clients.remove(client)
                                client.close()

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
                                'Boost': False
                            }
                        }

                        self.data.setDataJson(f'user[{username}].json', user)
                        client.send('Successfully signed up!'.encode('utf-8'))

                    except Exception as e:
                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                # SETTINGS
                if (request == 'SETTINGS REQUEST'):
                    try:
                        adjustment = client.recv(1024).decode('utf-8')
                        change = client.recv(1024).decode('utf-8')
                        
                        obj = self.users[self.clients.index(client)]
                        obj[adjustment] = change

                        self.data.setDataJson('user[{}].json'.format(obj['Username']), obj)
                        client.send('Successfully changed settings!'.encode('utf-8'))
                        
                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                    except Exception as e:
                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                # DELETE ACCOUNT
                if (request == 'DELETE ACCOUNT REQUEST'):
                    try:
                        os.remove('DataBase/user[{}].json'.format(self.users[self.clients.index(client)]["Username"]))
                        client.send('Account deleted successfully'.encode('utf-8'))

                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                    except Exception as e:
                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                # INFORMATION
                if (request == 'INFO REQUEST'):
                    try:
                        obj = self.users[self.clients.index(client)]
                        client.send(str(obj).encode('utf-8'))
                    except Exception as e:
                        index = self.clients.index(client)
                        client.close()
                        self.clients.remove(client)
                        self.users.remove(self.users[index])
                        break

                # BOOST
                if (request == 'BOOST REQUEST'):
                    pass

            except Exception as e:
                print(e)
                index = self.clients.index(client)
                client.close()
                self.clients.remove(client)
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            print(f'{client} connected with address: {address}.')

            self.clients.append(client)

            handling_thread = threading.Thread(target=self.handle_client, args=(client,))
            handling_thread.start()

    def start(self):
        print(f'Data Server listening on {HOST}...')
        self.receive()

if __name__ == '__main__':
    server = DataServer(HOST, PORT)
    server.start()