import string

def create_dict() -> dict:
    dict = {}
    alphabets = string.ascii_uppercase
    for count, letter in enumerate(alphabets):
        dict[letter] = count
    # print(dict)

    return dict


def get_key(ascii: [int]) -> str:
    for i in range(len(ascii)):
        for key, value in dict.items():
            if value == ascii[i]:
                ascii[i] = key
    return ascii


def cypher(message: str, key: int, mode: str) -> str:
    msg_num = [ dict.get(i) for i in message ]
    length = len(dict)

    if mode == "cypher":
        cypher_num = [ (num * key) % length for num in msg_num]
    elif mode == "decypher":
        key_inverse = pow(key, -1, 26)
        cypher_num = [ (num * key_inverse) % length for num in msg_num]
    
    return get_key(cypher_num)


dict = create_dict()
message = input("Enter a message: ").upper()
while True:
    key = int(input("Enter a key: "))
    if key in [3, 5, 7, 9]:
        break
print("message: ", message, "key: ", key)

cypher_message = cypher(list(message), key, "cypher")
print("cyphered: ", cypher_message)

print("Sending message...")

decyper_message = cypher(list(cypher_message), key, "decypher")
print("decyphered: ", decyper_message)


__all__ = [ "cypher" ]