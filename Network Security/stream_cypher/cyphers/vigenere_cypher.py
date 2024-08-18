import string

def create_matrix() -> [list]:

    matrix = []
    alphabets = [ letter for letter in string.ascii_uppercase ]

    for i in range(26):
        temp = [letter for letter in alphabets[i:]]
        if len(temp) != 26:
            temp += [letter for letter in alphabets[:i]]
        matrix.append(temp)

    # print(matrix)
    return matrix


def get_index(matrix, value):
    
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == value:
                return (i, j)
    
    return None 

def cypher(message: list, key: list, mode: str) -> str:
    
    matrix = create_matrix()
    alphabets = [ letter for letter in string.ascii_uppercase ]

    while len(key) != len(message):
        for letter in key:
            if len(key) == len(message):
                break
            key.append(letter)
    # print(key)

    if mode == "cypher":
        cypher = [ matrix[alphabets.index(i)][alphabets.index(j)] for i, j in zip(message, key)] 

    elif mode == "decypher":
        cypher = []
        for i, j in zip(message, key):

            col = []
            for sub_list in matrix:
                col.append(sub_list[alphabets.index(j)])
            
            for count, c in enumerate(col):
                if c == i:
                    cypher.append(alphabets[count])

    return ''.join(cypher)


message = str(input("Enter a message: ").upper())
key = str(input("Enter a key: ").upper())
print("message: ", message, "key: ", key)

cypher_message = cypher(list(message), list(key), "cypher")
print("cyphered: ", cypher_message)

print("Sending message...")

decyper_message = cypher(list(cypher_message), list(key), "decypher")
print("decyphered: ", decyper_message)


__all__ = [ "cypher" ]