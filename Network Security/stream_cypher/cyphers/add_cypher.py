import string

def create_dict() -> dict:
    dict = {}
    alphabets = string.ascii_letters + ' '
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


def cypher(message: str, key: int, mode: str) -> str:

    dict = create_dict()

    msg_num = [ dict.get(i) for i in message ]
    length = len(dict)

    if mode == "cypher":
        cypher_num = [ (num + key) % length for num in msg_num]
    elif mode == "decypher":
        cypher_num = [ (num - key) % length for num in msg_num]
    
    return ''.join(get_key(cypher_num, dict))


# message = input("Enter a message: ")
# key = int(input("Enter a key: "))
# print("message: ", message, "key: ", key)

# cypher_message = cypher(list(message), key, "cypher")
# print("cyphered: ", cypher_message)

# print("Sending message...")

# decyper_message = cypher(list(cypher_message), key, "decypher")
# print("decyphered: ", decyper_message)

