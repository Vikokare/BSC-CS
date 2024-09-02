coins=[];

coin_list=[];

n=int(input("Enter number of coins u want to enter: "));
for i in range(n):
	coin=int(input("Input coin: "));
	coin_list.append(coin);

Required_coin=int(input("Enter required amount: "));

a=sorted(coin_list);
a.reverse();
print("Entered list of coin are: ",a);

mini=min(coin_list)

if mini>Required_coin:
        print("The minimun coin is greater than the required amount")
        exit()
elif Required_coin<=0:
        print("invalid input")
        exit()

ind=[]

def co(j):
    Final=0
    for i in a :
            while Final <= Required_coin :
                    Final+=i;
                    coins.append(i);
                    if Final > Required_coin:
                            Final-=i;
                            coins.remove(i);
                            break;
    print("final coins are",coins)
    ind.append(len(coins))
    coins.clear()
    


for i in range(n):
    print("\n")
    co(a[0])
    a.remove(a[0])
d=ind.index(min(ind))
print("\n")
print("THE BEST SOLUTION OF CHANGES IS",d+1,"ONE")

                
                
        
                
