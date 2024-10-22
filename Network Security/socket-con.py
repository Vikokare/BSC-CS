import socket
import sys

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)
    print("Server is listening on port 12345...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        message = client_socket.recv(1024).decode()
        print("CLIENT:", message)

        client_socket.send(str(input("SERVER: ")).encode())

    client_socket.close()
    server_socket.close()


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected...")

    while True:
        client_socket.send(str(input("CLIENT: ")).encode())
        
        response = client_socket.recv(1024).decode()
        print("SERVER:", response)

    client_socket.close()


if sys.argv[1] == 'server':
    start_server()
elif sys.argv[1] == 'client':
    start_client()
else:
    start_server()