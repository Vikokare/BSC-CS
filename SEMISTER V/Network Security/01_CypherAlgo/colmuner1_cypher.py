def split_array(arr: [int], size: int) -> [list]:
    final_array = []
    while len(arr) > size:
        pice = arr[:size]
        final_array.append(pice)
        arr = arr[size:]
    final_array.append(arr)

    for array in final_array:
        while len(array) != size:
            array.extend("#")
        
    return final_array

def create_dict(matrix: [list], keyword: [str], mode: str) -> dict:
    dict = {}
    # print(matrix, keyword)
    if mode == "cypher":    
        for count, key in enumerate(keyword, 0):
            arr = []
            for i in range(len(matrix)):
                # print(count, key, i)
                arr.append(matrix[i][count])
            dict[key] = arr
    elif mode == "decypher":
        for count, key in enumerate(sorted(keyword)):    
            dict[key] = matrix[count]

    return dict


def cypher(message: list, keyword: [int], length: int, mode: str) -> str:

    matrix = split_array(message, length)
    # print("-----", matrix)

    dict = create_dict(matrix, keyword, mode)
    # print(dict)
    
    if mode == "cypher":
        message = ""
        for i in sorted(keyword):
            message += ''.join(dict.get(i))
    elif mode == "decypher":
        message = ""
        for l in range(length):
            for key in keyword:
                message += dict.get(key)[l]

        message = ''.join([i for i in message if i != '#'])


    return message, len(matrix)


message = str(input("Enter a message: "))
while True:
    keyword = str(input("Enter a key: "))
    if len(keyword) < len(message):
        break
    print(f"Key must be less that the length of the {len(message)}, Please enter key again...")
print("message: ", message, " key: ", keyword)

cypher_message, length = cypher(list(message), list(keyword), len(keyword), "cypher")
print("cyphered: ", cypher_message)

print("Sending message...")

decyper_message, length = cypher(list(cypher_message), list(keyword), length, "decypher")
print("decyphered: ", decyper_message)
