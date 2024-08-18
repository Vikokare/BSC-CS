def split_array(arr: [int], size: int) -> [list]:
    final_array = []
    while len(arr) > size:
        pice = arr[:size]
        final_array.append(pice)
        arr = arr[size:]
    final_array.append(arr)

    for array in final_array:
        while len(array) != key:
            array.extend("#")
        
    return final_array


def cypher(message: str, key: int, mode: str) -> str:

    matrix = split_array(message, key)

    message = []
    if mode == "cypher":    
        for i in range(key):
            for j in range(len(matrix)):
                message.append(matrix[j][i])
    elif mode == "decypher":
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                message.append(matrix[j][i])
        
        message = [i for i in message if i != '#']
            
    return ''.join(message), len(matrix)



# message = input("Enter a message: ")
# while True:
#     key = int(input("Enter a key: "))
#     if key < len(message):
#         break
#     print(f"Key must be less that the length of the {len(message)}, Please enter key again...")

# print("message: ", message, " key: ", key)

# cypher_message, key = cypher(list(message), key, "cypher")
# print("cyphered: ", cypher_message)

# print("Sending message...")

# decyper_message, key = cypher(list(cypher_message), key, "decypher")
# print("decyphered: ", decyper_message)
