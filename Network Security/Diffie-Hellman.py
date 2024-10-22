import random

# Power function to return value of a^b mod P
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

prime = set()
def prime_filler():
    seive = [True] * 250
    seive[0] = seive[1] = False

    for i in range(2, 250):
        for j in range(i*2, 250, i):
            seive[j] = False
    
    for i in range(len(seive)):
        if seive[i]:
            prime.add(i)


def pick_random_prime():
    global prime
    temp_prime = list(prime)
    k = random.randint(0, len(prime) - 1)
    return temp_prime[k]

# smallest primitive root of a prime P
def find_primitive_root(p):
    if p == 2:
        return 1 # The only primitive root for prime 2 is 1
    
    # Create a list of remainders modulo p
    required_set = {num for num in range(1, p)}

    for g in range(2, p):
        actual_set = {power(g, powers, p) for powers in range(1, p)}
        if required_set == actual_set:
            return g
    
    # In case no primitive root is found (though this shouldn't happen for primes)
    return -1

# Main Diffie-Hellman function
def main():
    prime_filler()

    random_prime = pick_random_prime()
    print("The value of random_prime", random_prime)

    random_primitive_root = find_primitive_root(random_prime)
    print("Primitive root of random_prime:", random_primitive_root)

    alice_private_key = random.randint(1, random_prime - 1)
    print("Alice Private key:", alice_private_key)

    alice_public_key = power(random_primitive_root, alice_private_key, random_prime)

    bob_private_key = random.randint(1, random_prime - 1)
    print("Bob private key:", bob_private_key)

    bob_public_key = power(random_primitive_root, bob_private_key, random_prime)

    alice_secret_key = power(bob_public_key, alice_private_key, random_prime)
    bob_secret_key = power(alice_public_key, bob_private_key, random_prime)

    print("Alice secret key:", alice_secret_key)
    print("Bob secret key:", bob_secret_key)

main()
