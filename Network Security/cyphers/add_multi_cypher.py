import string

def create_dict() -> dict:
    dict = {}
    alphabets = string.ascii_uppercase # string.letter + ' '
    for count, letter in enumerate(alphabets):
        dict[letter] = count
    # print(dict)

    return dict


def get_key(ascii: [int], dict) -> str:
    for i in range(len(ascii)):
        for key, value in dict.items():
            if value == ascii[i]:
                ascii[i] = key
    return ascii


def cypher(message: str, add_key: int, mul_key: int, mode: str) -> str:
    dict = create_dict()
    msg_num = [ dict.get(i) for i in message ]
    length = len(dict)

    if mode == "cypher":
        cypher_num = [ ((num + add_key) * mul_key) % length for num in msg_num]
    elif mode == "decypher":
        mul_key_inverse = pow(mul_key, -1, 26)
        cypher_num = [ ((num * mul_key_inverse) - add_key ) % length for num in msg_num]
    
    return ''.join(get_key(cypher_num, dict))



# message = input("Enter a message: ").upper()
# add_key = int(input("Enter a add key: "))
# while True:
#     mul_key = int(input("Enter a mul key: "))
#     if mul_key in [3, 5, 7, 9]:
#         break
#     print(f"Key must be [3, 5, 7, 9], Please enter key again...")
# print("message: ", message, "add key: ", add_key, "mul key: ", mul_key)

# cypher_message = cypher(list(message), add_key, mul_key, "cypher")
# print("cyphered: ", cypher_message)

# print("Sending message...")

# decyper_message = cypher(list(cypher_message), add_key, mul_key, "decypher")
# print("decyphered: ", decyper_message)
