import threading, socket

HOST = '127.0.0.1'
PORT = 9000

class DataServer:
    def __init__(self, host, port):
        self.host, self.port = host, port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()

        self.clients = []
        self.usernames = []
        self.passwords = []

    def handle_client_login(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'LOGIN REQUEST'):
                    pass

                continue

            except Exception:
                pass

    def handle_client_sign_up(self, client):
        while (True):
            try:
                request = client.recv(1024).decode('utf-8')

                if (request == 'SIGN UP REQUEST'):
                    pass

            except Exception:
                pass

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
                    pass

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
        
        login_thread.start()
        sign_up_thread.start()
        settings_thread.start()
        del_acc_thread.start()


    def send(self, client, message):
        cli = self.clients[client]
        cli.send(message.encode('utf-8'))