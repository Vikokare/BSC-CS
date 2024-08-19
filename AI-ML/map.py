import pandas as pd


data = [    
    ['', 1, 0, 0, 0, 0],
    [1, '', 1, 0, 1, 0],
    [0, 1, '', 1, 0, 0],
    [0, 0, 1, '', 1, 1],
    [0, 1, 0, 1, '', 1],
    [0, 0, 0, 1, 1, ''] 
]
header = ["Devgad", "Malvan", "Oros", "Kudal", "vengurla", "sawantawadi"]
df = pd.DataFrame(data, index=header, columns=header )
print(df)


def brute_force(df, currect, destination):
    ...


print("\nselect the currect place and destination: ")
for count, place in enumerate(header):
    print(f"{count}: {place}")

while True:
    current = int(input("Enter the current cord: "))
    if current < len(header):
        break
    print("Please, Try again...")

while True:
    destination = int(input("Enter the destination cord: "))
    if destination < len(header):
        break
    print("Please, Try again...")

print(f"Searching a route from {header[current]} to {header[destination]}")


brute_force(df, current, destination)