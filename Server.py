import socket
import re

SERVER_PORT = 6981
NUM_BYTES = 1024
NUM_REQUESTS_ALLOWED = 5


class Server:
    login_info = ''
    client_message = ''
    file = ''
    found = 'False'
    client_socket = ''
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        pass

    def listen(self):
        self.server_socket.bind((socket.gethostname(), SERVER_PORT))
        self.server_socket.listen(NUM_REQUESTS_ALLOWED)
        while True:
            self.client_socket, address = self.server_socket.accept()
            self.client_message = self.client_socket.recv(NUM_BYTES)
            self.client_message = self.client_message.decode('utf-8')
            self.parse_command()

    def parse_command(self):
        if re.search('LOGIN', self.client_message):
            self.login()
        elif re.search('SOLVE', self.client_message):
            self.solve()
        elif re.search('SHUTDOWN', self.client_message):
            self.shutdown()
        elif re.search('LOGOUT', self.client_message):
            self.logout()
        else:
            self.client_socket.send(bytes('301 message format error', 'utf-8'))

    def login(self):
        with open('logins.txt', 'r') as file_descriptor:
            line = file_descriptor.readline()
            while line != '':
                result = re.search(line.strip(), self.client_message)
                if result:
                    self.found = 'True'
                    self.login_info = self.client_message
                line = file_descriptor.readline()
        self.client_socket.send(bytes(self.found, 'utf-8'))

    def solve(self):
        print(self.login_info)

    def logout(self):
        self.login_info = ''
        self.client_socket.send(bytes('200 OK', 'utf-8'))

    def shutdown(self):
        self.client_socket.send(bytes('200 OK', 'utf-8'))
        self.server_socket.shutdown(socket.SHUT_RDWR)


server = Server()
server.listen()


