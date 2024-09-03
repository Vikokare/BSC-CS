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


def breath_search(map, current, destination):

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


def depth_search(map, current, destination):

    search_stack = [current]
    route = [current]

    # while current != destination:
    for i in range(5):    
        print(' -> '.join(route))
        
        if destination in map[current]:
            route.append(destination)
            # break

        for place in map[current]:
            if place not in search_stack:
                print("--", place)
                search_stack.append(place)
        
        print(search_stack)
        current = search_stack.pop()
    




print("\nselect the currect place and destination: ")
for count, place in enumerate(header):
    print(f"{count}: {place}")

while True:
    current = 0 #int(input("Enter the current cord: "))
    if current < len(header):
        current = header[current]
        break
    print("Please, Try again...")

while True:
    destination = 5 #int(input("Enter the destination cord: "))
    if destination < len(header):
        destination = header[destination]
        break
    print("Please, Try again...")

print(f"Searching a route from {current} to {destination}")


# breath_search(map, current, destination)
depth_search(map, current, destination)