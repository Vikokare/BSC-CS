import sys
import hmac
import hashlib
import socket

def generate_mac(secret_pass, message):
    return hmac.new(secret_pass.encode(), message.encode(), hashlib.sha256).hexdigest()

def verify_mac(secret_pass, message, received_mac):
    generated_mac = generate_mac(secret_pass, message)
    return hmac.compare_digest(generated_mac, received_mac)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)
    print("Server is listening on port 12345...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    secret_pass = str(input("Enter your shared password: "))

    while True:
        message_mac = client_socket.recv(1024).decode().split(",")
        print(message_mac)
        message = message_mac[0]
        received_mac = message_mac[1]

        boolean = verify_mac(secret_pass, message, received_mac)

        if not boolean:
            client_socket.close()
            server_socket.close()
            return 
        
        print("CLIENT:", message)

        response = str(input("SERVER: "))
        response_mac = generate_mac(secret_pass, response)
        client_socket.send(f"{response},{response_mac}".encode())

    client_socket.close()
    server_socket.close()


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected...")

    secret_pass = str(input("Enter your shared password: "))

    while True:
        message = str(input("CLIENT: "))
        message_mac = generate_mac(secret_pass, message)
        client_socket.send(f"{message},{message_mac}".encode())
        
        response_mac = client_socket.recv(1024).decode().split(",")
        print(response_mac)
        response = response_mac[0]
        received_mac = response_mac[1]

        boolean = verify_mac(secret_pass, response, received_mac)
        if not boolean:
            client_socket.close()
            return
        
        print("SERVER:", response)

    client_socket.close()


if sys.argv[1] == 'server':
    start_server()
elif sys.argv[1] == 'client':
    start_client()
else:
    start_server()