# Searching Algorithm

# linear search
list=[3,2,22,12,23,23,34,54,]   
def find(a):
    for i in list:
        if a not in list:
            print("no search result")
        elif i == a :
            print("number", a,"is at position ",list.index(i)+1)
 
n=int(input("enter the number u want to find: "))
find(n)


# Binary search #2
def search(list, num, start=0) :
    mid = len(list)//2
    end = len(list) - 1

    print(list, list[start], list[mid], list[end])

    if list[mid] == num :
        print("The number is at index", mid)
    
    elif list[mid] > num :
        search(list[:mid], num)
        
    elif list[mid] < num :
        search(list[mid:], num)


search([0,1,2,3,4,5,6,7,8,9,10], int(input("Search for: ")))



