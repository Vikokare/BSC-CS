## -------------------------------------------------------------Accept three consecutive one 
def transitions(current_state, current_symbol) :
    transition = {
        ('q0', '0') : 'q0',
        ('q0', '1') : 'q1',
        ('q1', '0') : 'q0',
        ('q1', '1') : 'q2',
        ('q2', '0') : 'q0',
        ('q2', '1') : 'q3',
        ('q3', '0') : 'q0',
        ('q3', '1') : 'q3',
    }

    return transition.get((current_state, current_symbol))

## Main script
def main(current_state, final_state, test) :
    states = [current_state]
    
    for symbol in test :
        current_state = transitions(current_state, symbol)
        states.append(current_state)
    print(test,' --> '.join(states))
    
    if current_state == '' : return False
    return current_state == final_state

current_state = 'q0'
final_state = 'q3'

for test in ['100', '0101', '1010', '1111'] :
    print("Accepted : ", main(current_state, final_state, test))
