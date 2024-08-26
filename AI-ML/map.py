import pandas as pd


header = ["Devgad", "Malvan", "Oros", "Kudal", "Vengurla", "Sawantawadi"]
map = {
    "Devgad":       [ "Malvan" ],
    "Malvan":       [ "Devgad", "Oros", "Vengurla" ],
    "Oros":         [ "Malvan", "Kudal"],
    "Kudal":        [ "Oros", "Vengurla", "Sawantawadi" ],
    "Vengurla":     [ "Malvan", "Kudal", "Sawantawadi" ],
    "Sawantawadi":  [ "Kudal", "Vengurla" ],
}
print(map)



def brute_force(map, current, destination):

    route = [current]
    visited_places = [current]
    search_stack = []

    while current != destination:

        print(' -> '.join(route))
        
        if destination in map[current]:
            route.append(destination)
            break
        
        for place in map[current]:
            if place not in visited_places:
                print("-", place)
                search_stack.append(place)
        
        print("search next:", search_stack)
        print("visited_places: ", visited_places, "\n")

        current = search_stack.pop(0)
        visited_places.append(current)
        route.append(current)
    
    print(' -> '.join(route))



print("\nselect the currect place and destination: ")
for count, place in enumerate(header):
    print(f"{count}: {place}")

while True:
    current = int(input("Enter the current cord: "))
    if current < len(header):
        current = header[current]
        break
    print("Please, Try again...")

while True:
    destination = int(input("Enter the destination cord: "))
    if destination < len(header):
        destination = header[destination]
        break
    print("Please, Try again...")

print(f"Searching a route from {current} to {destination}")



brute_force(map, current, destination)