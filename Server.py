import socket
import re

SERVER_PORT = 6972
NUM_BYTES = 1024
NUM_REQUESTS_ALLOWED = 5


class Server:
    login_info = ''
    client_message = ''
    file = ''
    found = 'False'
    client_socket = ''
    error_message = '301 message format error'
    not_logged_in = 'Error: you are not signed in, Please sign in and try again'
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self):
        pass

    # Function to listen for a message sent from the client
    # it decodes and sends the decoded message to parse_command
    def listen(self):
        self.server_socket.bind((socket.gethostname(), SERVER_PORT))
        self.server_socket.listen(NUM_REQUESTS_ALLOWED)
        while True:
            self.client_socket, address = self.server_socket.accept()
            self.client_message = self.client_socket.recv(NUM_BYTES)
            self.client_message = self.client_message.decode('utf-8')
            self.parse_command()

    # Function that takes in the decoded message and
    # regex the message to find the command the user
    # wants to use and then hands it off to the
    # respective function
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
            self.client_socket.send(bytes(self.error_message, 'utf-8'))

    # Function that implements the login command
    # it uses regex to search the login.txt
    # file to match with users that can login
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

    # Function the implements the solve command
    # pulls the numbers from the string sent over
    # from the client and the regex to find whether
    # to solve a circle or a rectangle. it also opens
    # up a file bound to the user and writes and
    # writes the computation
    def solve(self):
        if self.login_info != '':  # make sure the user is logged in
            user_name = self.login_info.split()
            user_name = user_name[1]
            user_name += '_solutions.tx'
            res = [int(i) for i in self.client_message.split() if i.isdigit()]  # find the numbers in the string
            if re.search('-c', self.client_message) and len(res) > 0:
                circumference, area = self.circle(res)
                message = 'Circle’s circumference is ' + str("%.2f" % circumference) + ' and ' \
                                                                                       'area is ' + str("%.2f" % area)
            elif re.search('-r', self.client_message) and len(res) > 0:
                perimeter, area = self.rectangle(res)
                message = 'Rectangle’s perimeter is ' + str("%.2f" % perimeter) + ' and ' \
                                                                                  'area is ' + str("%.2f" % area)
            else:
                message = 'Error: No sides or radius'
            self.client_socket.send(bytes(message, 'utf-8'))
            self.write_to_file(user_name, message)
        else:
            self.client_socket.send(bytes(self.not_logged_in, 'utf-8'))

    # Function that implements the logout command
    # it allows the user to terminate the client
    # while keeping the server running
    def logout(self):
        self.login_info = ''
        self.client_socket.send(bytes('200 OK', 'utf-8'))

    # Function that implements the shutdown command
    # it allows the user to terminate the client and
    # the Server
    def shutdown(self):
        self.client_socket.send(bytes('200 OK', 'utf-8'))
        self.server_socket.shutdown(socket.SHUT_RDWR)

    # Helper function to compute the circumference
    # and the area of a circle
    def circle(self, radius) -> float:
        circumference = 2*3.14*radius[0]
        area = 3.14*radius[0]**2
        return circumference, area

    # Helper function to computer the perimeter
    # and area of a rectangle if the use inputs 2
    # sides, else computes based on a square
    def rectangle(self, sides) -> float:
        perimeter = 2*(sides[0] + sides[0])
        area = sides[0] * sides[0]
        return perimeter, area

    # Helper function to write the solution to
    # a file with respect to who is signed in
    def write_to_file(self, file, message):
        f = open(file, "a")
        f.write(message + "\n")
        f.close()


server = Server()
server.listen()
