
## -------------------------------------------------------------equal no of 1 and 0
def transitions(current_state, symbol) :
    transition = {
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q1',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q1',
    }
    return transition.get((current_state, symbol))

def run(input_string, current_state, final_state) :
    zero, one = 0, 0
    states = [current_state]

    for inp in input_string:
        if inp == '0': zero+=1
        if inp == '1': one+=1

        current_state = transitions(current_state, inp)
        states.append(current_state)
    
    print( ' --> '.join(states))
    print('Zeros :', zero, 'Ones :', one)
    if current_state == '' : return False
    return zero == one


initial_state = "q0"
final_state = "q2"
input_strings = ['00', '01', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010']
for input_string in input_strings:
    print("Input:", input_string,"Accepted:", run(input_string, initial_state, final_state))
