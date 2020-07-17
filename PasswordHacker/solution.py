import sys
import socket

class PasswordHacker:

    def __init__(self):
        self.get_params()


    def get_params(self):
        self.ip_address = sys.argv[1]
        self.port = int(sys.argv[2])
        self.message = sys.argv[3]

    def make_request(self):
        with socket.socket() as hack_socket:
            hack_socket.connect((self.ip_address, self.port))
            hack_socket.send(self.message.encode())
            self.response_raw = hack_socket.recv(1024)
            self.response = self.response_raw.decode()
    def show_response(self):
        print(self.response)


hack = PasswordHacker()
hack.make_request()
hack.show_response()





