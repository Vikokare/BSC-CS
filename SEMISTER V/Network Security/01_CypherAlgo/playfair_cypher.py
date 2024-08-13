import string
import random

# def create_matrix():
#     matrix = [[] for _ in range(5)]
#     complete_alpha = ""
#     for list in matrix:
#         while len(list) != 5: 
#             letter = random.choice(string.ascii_uppercase)
#             if letter not in complete_alpha:
#                 list.append(letter)
#                 complete_alpha += letter
#     print(matrix)
#     return matrix

def create_matrix(keyword: str):
    matrix = [[] for _ in range(5)]
    complete_alpha =[]

    for l in keyword:
        complete_alpha.append(l)

    for l in string.ascii_lowercase:
        if l == 'j':
            continue
        if l not in complete_alpha:
            complete_alpha.append(l)
    
    for list in matrix:
        while len(list) != 5:
            list.append(complete_alpha.pop(0))
    
    # print(matrix)
    return matrix
                   

def split_array(arr: [int], size = 2) -> [list]:
    final_array = []

    while len(arr) > size:
        pice = arr[:size]
        final_array.append(pice)
        arr = arr[size:]
    final_array.append(arr)

    # select random letter not in msg
    for array in final_array:
        while len(array) != size:
            array.extend("z")

    # print(final_array)
    return final_array


def get_index(matrix, value):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if element == value:
                return (i, j)
    return None  # Value not found

def rules(ind: list, mode):
    if mode == "cypher":
        if ind[0][1] == ind[1][1]:
            values = a, b, x, y = [ind[0][0]+1, ind[0][1], ind[1][0]+1, ind[1][1]]
        if ind[0][0] == ind[1][0]:
            values = a, b, x, y = [ind[0][0], ind[0][1]+1, ind[1][0], ind[1][1]+1]
        if ind[0][1] != ind[1][1] and ind[0][0] != ind[1][0]:
            values = a, b, x, y = [ind[0][0], ind[1][1], ind[1][0], ind[0][1]]

        for count, val in enumerate(values):
            if val > 4:
                values[count] = val - 5

    elif mode == "decypher":
        if ind[0][1] == ind[1][1]:
            values = a, b, x, y = [ind[0][0]-1, ind[0][1], ind[1][0]-1, ind[1][1]]
        if ind[0][0] == ind[1][0]:
            values = a, b, x, y = [ind[0][0], ind[0][1]-1, ind[1][0], ind[1][1]-1]
        if ind[0][1] != ind[1][1] and ind[0][0] != ind[1][0]:
            values = a, b, x, y = [ind[0][0], ind[1][1], ind[1][0], ind[0][1]]

        for count, val in enumerate(values):
            if val > 4:
                values[count] = val - 5

    return [(values[0], values[1]), (values[2], values[3])]

def cypher(message: list, keyword: str, mode: str) -> str:
    matrix = create_matrix(keyword)
    msg_array = split_array(message)

    index = []
    for list in msg_array:
        index.append([get_index(matrix, list[0]), get_index(matrix, list[1])])
    # print(index)

    updated_index_array = []
    for ind in index:
        updated_index_array.append(rules(ind, mode))
    
    final_string = ""
    for ind in updated_index_array:
        final_string += matrix[ind[0][0]][ind[0][1]]
        final_string += matrix[ind[1][0]][ind[1][1]]

    return final_string

message = str(input("Enter a message: "))
keyword = str(input("Enter a key: "))
cypher_message = cypher(list(message), keyword, "cypher")
print("cyphered: ", cypher_message)

print("Sending message...")

decyper_message = cypher(list(cypher_message), keyword, "decypher")
print("decyphered: ", decyper_message.replace('z', ''))
