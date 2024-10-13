
header = ["Devgad", "Malvan", "Oros", "Kudal", "Vengurla", "Sawantawadi"]
map = {
    "Devgad":       [ "Malvan" ],
    "Malvan":       [ "Devgad", "Oros", "Vengurla" ],
    "Oros":         [ "Malvan", "Kudal"],
    "Kudal":        [ "Oros", "Vengurla", "Sawantawadi" ],
    "Vengurla":     [ "Malvan", "Kudal", "Sawantawadi" ],
    "Sawantawadi":  [ "Kudal", "Vengurla" ],
}

def breath_first_search(current, destination):
    search_stack = [current]
    visited_places = set([current])
    parent_map = { current: None }
    
    while search_stack:
        current = search_stack.pop(0)
        visited_places.add(current)

        if current == destination:
            break

        for neighbor in map[current]:
            if neighbor not in search_stack and neighbor not in visited_places:
                search_stack.append(neighbor)
                parent_map[neighbor] = current
    print(parent_map)

    if destination in parent_map:
        route = [destination]
        curr = destination
        while curr is not None:
            curr = parent_map.get(curr)
            route.append(curr)
        route.pop()
        route.reverse()

    print(" --> ".join(route))


def depth_first_search(current, destination):
    search_stack = [current]
    visited_places = set([current])
    parent_map = { current: None }
    
    while search_stack:
        current = search_stack.pop()
        visited_places.add(current)

        if current == destination:
            break

        for neighbor in map[current]:
            if neighbor not in search_stack and neighbor not in visited_places:
                search_stack.append(neighbor)
                parent_map[neighbor] = current
    print(parent_map)

    if destination in parent_map:
        route = [destination]
        curr = destination
        while curr is not None:
            curr = parent_map.get(curr)
            route.append(curr)
        route.pop()
        route.reverse()

    print(" --> ".join(route))

breath_first_search('Sawantawadi', 'Devgad')
# depth_first_search('Devgad', 'Sawantawadi')