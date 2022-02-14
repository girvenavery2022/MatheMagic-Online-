import socket
import re

SERVER_PORT = 6973
NUM_BYTES = 1024


class Client:
    server_message = ''
    client_message = ''

    def __init__(self):
        pass

    # Function that asks the user for a command
    # to send to the server and waits for a response
    # back. As long as the server doesn't echo back
    # 200 OK, it continues to ask, send and listen.
    def command(self):
        while self.server_message != '200 OK':
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((socket.gethostname(), SERVER_PORT))
            self.client_message = input()
            client_socket.send(bytes(self.client_message, 'utf-8'))
            self.server_message = client_socket.recv(NUM_BYTES)
            self.server_message = self.server_message.decode('utf-8')
            if re.search('LOGIN', self.client_message):
                if re.search('True', self.server_message):
                    print('SUCCESS')
                else:
                    print('FAILURE: Please provide correct username and password.Try again.')
            else:
                print(self.server_message)


client = Client()
client.command()
