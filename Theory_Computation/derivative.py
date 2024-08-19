## -------------------------------------------------------------Generating derivation sequence
def productions(symbol) :
    production = {
        'S' : 'AB',
        'A' : 'a',
        'B' : 'b',
    }

    return production.get(symbol)

def main(current_string, final_string) :
    states = [current_string]
    
    for symbol in ['S', 'A', 'B'] :
        current_string = current_string.replace(symbol, productions(symbol))
        states.append(current_string)
    print(' --> '.join(states))
    
    return current_string == final_string

current_string = 'S'
final_string = 'ab'
print("Accepted:", main(current_string, final_string))
