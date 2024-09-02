#fibonasis_addition
def fib_add(list,i=0, limit=16):
    if len(list) == limit:
        return list
    list.append(list[i] + list[i+1])
    return fib_add(list,i+1)

print("fibonasis_addition: ", fib_add([0,1]))


# fibonasis_multiplication
def fib_mux(list, i=0, limit=10):
    if len(list) == limit:
        return list
    list.append(list[i] * list[i+1])
    return fib_mux(list, i+1)

print("fibonasis_multiplication: ",fib_mux([1,2]))



