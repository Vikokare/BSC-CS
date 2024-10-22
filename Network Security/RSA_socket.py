import socket
import sys
import random
import math
import ast

def generate_primes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return {i for i in range(limit) if sieve[i]}

def pick_random_prime(primes):
    prime_list = list(primes)
    random.shuffle(prime_list)
    return random.choice(list(prime_list))

def choose_e(fi):
    e = 2
    while math.gcd(e, fi) != 1:
        e += 1
    return e

def set_keys():
    primes = generate_primes(250)
    prime1 = pick_random_prime(primes)
    prime2 = pick_random_prime(primes)
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)

    # Choose e
    e = choose_e(fi)

    # Calculate d
    d = pow(e, -1, fi)
    
    print("PRIVATE KEY:", d)
    print("PUBLIC KEY:", e)

    return e, d, n 

def encrypt(message, public_key, n):
    return [pow(ord(letter), public_key, n) for letter in message]

def decrypt(encrypted_text, private_key, n):
    return ''.join(chr(pow(num, private_key, n)) for num in encrypted_text)

# public_key, private_key, n = set_keys()
# message = "Hello"
# encrypted = encrypt(message, public_key, n)
# print("Encrypted:", encrypted)
# decrypted = decrypt(encrypted, private_key, n)
# print("Decrypted:", decrypted)


def start_server():
    public_key, private_key, n = set_keys()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    server_keys = client_socket.recv(1024).decode()
    client_public_key, client_n = server_keys.split(",")
    print("CLIENT PUBLIC KEY:", client_public_key)
    print("CLIENT MODULO KEY:", client_n)

    client_socket.send(f"{public_key},{n}".encode())
    
    while True:
        encrypted_text = client_socket.recv(1024).decode()
        message = decrypt(ast.literal_eval(encrypted_text), private_key, n)
        print("CLIENT:", message)

        msg = encrypt(str(input("SERVER: ")), int(client_public_key), int(client_n))
        client_socket.send(str(msg).encode())

    client_socket.close()
    server_socket.close()


def start_client():
    public_key, private_key, n = set_keys()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected...")

    client_socket.send(f"{public_key},{n}".encode())

    server_keys = client_socket.recv(1024).decode()
    server_public_key, server_n = server_keys.split(",")
    print("SERVER PUBLIC KEY:", server_public_key)
    print("SERVER MODULO KEY:", server_n)

    while True:
        msg = encrypt(str(input("SERVER: ")), int(server_public_key), int(server_n))
        client_socket.send(str(msg).encode())
        
        encrypted_text = client_socket.recv(1024).decode()
        message = decrypt(ast.literal_eval(encrypted_text), private_key, n)

        print("SERVER:", message)

    client_socket.close()


if sys.argv[1] == 'server':
    start_server()
elif sys.argv[1] == 'client':
    start_client()
else:
    start_server()