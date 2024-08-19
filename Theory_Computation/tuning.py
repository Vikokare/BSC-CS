# ## -------------------------------------------------------------Tuning machine 1
# def transitions(current_state, symbol) :
#     transition = {
#         ('q0', '0'): ('q0', '0', 'R'),
#         ('q0', '1'): ('q1', '1', 'R'),
#         ('q0', 'B'): ('qacc', 'B', 'B'),
#         ('q1', '1'): ('q1', '1', 'R'),
#         ('q1', 'B'): ('qacc', 'B', 'B'),
#         ('qacc', 'B'): ('qfinal', 'B', 'B'),
#     }

#     return transition.get((current_state, symbol))

# current_string = ['B', 'B', 'q0', '0', '0', '0', '1', '1', '1', 'B', 'B']



# ## -------------------------------------------------------------Tuning machine 2
def transitions(current_state, symbol) :
    transition = {
        ('q0', '0'): ('q1', '0', 'R'),
        ('q1', '0'): ('q1', '0', 'R'),
        ('q1', '1'): ('q2', '1', 'R'),
        ('q2', '0'): ('q1', '0', 'R'),
        ('q2', '1'): ('q2', '1', 'R'),
        ('q2', 'B'): ('qacc', 'B', 'B'),
        ('qacc', 'B'): ('qfinal', 'B', 'B'),
    }

    return transition.get((current_state, symbol))


def main(current_string, current_state, final_state) :
    while current_state != 'qfinal' :
        print(current_string)

        ind = current_string.index(current_state)

        try :
            # get table values
            current_state, change, direction = transitions(current_state, current_string[ind + 1])
        except :
            return False

        # replace with new values
        current_string[ind], current_string[ind + 1] = current_state, change

        # swap values according to direction
        if direction == 'R' :
            current_string[ind], current_string[ind + 1] = current_string[ind + 1], current_string[ind]
        elif direction == 'L' :
            current_string[ind], current_string[ind - 1] = current_string[ind - 1], current_string[ind]

    print(current_string)
    return current_state == 'qfinal'


current_string = ['B', 'B', 'q0', '0', '1', '0', '1', 'B', 'B']
current_state = 'q0'
final_state = 'qfinal'
print("Accepted :",main(current_string, current_state, final_state))


