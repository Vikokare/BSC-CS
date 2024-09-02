#INSERTION SORT
list=[]
sorted_list=[]

num=int(input("Enter the number of values you wish to enter: "));
for l in range(num):
   list.append(int(input("enter the value: ")));
print(list)

while list:
   num=list[0]
   for i in list:
       if i<num:
           num=i
   sorted_list.append(num)
   list.remove(num)
   print(sorted_list)


#BUBBLE SORT
list=[]
num=int(input("Enter the number of values you wish to enter: "));
for l in range(num):
   list.append(int(input("enter the value: ")));
print(list)

def sort(list):
    for i in range(len(list)):
        for j in range(i,len(list)):
            if list[i] > list[j]:
                list[i] , list[j] = list[j] , list[i]
        print(list)
    return list
        
print("The sorted list is : ",sort(list))