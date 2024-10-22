import sys
import random
import socket
import cyphers.add_cypher as cyp

def power(a, b, p):
    return pow(a, b, p)


def prime_filler():
    seive = [True] * 250
    seive[0] = seive[1] = False
    for i in range(2, 250):
        for j in range(i*2, 250, i):
            seive[j] = False
    return {i for i in range(len(seive)) if seive[i]}


def pick_random_prime(prime_set):
    return random.choice(list(prime_set))


def find_primitive_root(p):
    if p == 2:
        return 1
    required_set = {num for num in range(1, p)}
    for g in range(2, p):
        actual_set = {power(g, powers, p) for powers in range(1, p)}
        if required_set == actual_set:
            return g
    return -1


def derive_key(shared_secret):
    return Fernet.generate_key()


def start_server():
    prime_set = prime_filler()
    random_prime = pick_random_prime(prime_set)
    random_primitive_root = find_primitive_root(random_prime)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    client_socket.send(f"{random_prime},{random_primitive_root}".encode())

    client_public_key = int(client_socket.recv(1024).decode())
    print("client public key:", client_public_key)

    server_private_key = random.randint(1, random_prime - 1)
    server_public_key = power(random_primitive_root, server_private_key, random_prime)
    print("Server public key:", server_public_key)

    client_socket.send(str(server_public_key).encode())

    shared_secret_key = power(client_public_key, server_private_key, random_prime)
    print("Server shared secret key:", shared_secret_key)

    while True:
        response = client_socket.recv(1024).decode()
        print("Encrypted msg:", response)
        response = cyp.cypher(response, shared_secret_key, "decypher")
        print("CLIENT:", response)

        message = cyp.cypher(str(input("SERVER: ")), shared_secret_key, "cypher")
        client_socket.send(message.encode())

    client_socket.close()
    server_socket.close()


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to server...")

    data = client_socket.recv(1024).decode()
    random_prime, random_primitive_root = map(int, data.split(","))
    print("Received prime:", random_prime)
    print("Received primitive root:", random_primitive_root)

    client_private_key = random.randint(1, random_prime - 1)
    client_public_key = power(random_primitive_root, client_private_key, random_prime)
    print("Client public key:", client_public_key)

    client_socket.send(str(client_public_key).encode())

    server_public_key = int(client_socket.recv(1024).decode())
    print("server public key:", server_public_key)

    shared_secret_key = power(server_public_key, client_private_key, random_prime)
    print("Client shared secret key:", shared_secret_key)

    while True:
        message = cyp.cypher(str(input("SERVER: ")), shared_secret_key, "cypher")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print("Encrypted msg:", response)
        response = cyp.cypher(response, shared_secret_key, "decypher")
        print("SERVER:", response)

    client_socket.close()


if __name__ == "__main__":
    if sys.argv[1] == 'server':
        start_server()
    elif sys.argv[1] == 'client':
        start_client()
    else:
        start_server()