import socket


def client():
    # Create client socket (AF_INET => IP, SOCK_STREAM => TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('127.0.0.1', 12345))
    user_input = input("What do you want to ask? : ")
    server.send(user_input.encode())
    response = server.recv(4096)
    server.close()
    print(response.decode())


if __name__ == '__main__':
    while True:
        client()
