def TowerOfHanoi(n,scouce,destination,auxilary):

    if n == 0:
        return

    TowerOfHanoi(n-1, scouce, auxilary, destination)

    print("Move disk", n, "from rod", scouce, "to rod", destination)

    TowerOfHanoi(n-1,auxilary,destination,scouce)


N=int(input("enter the number of disk"))

TowerOfHanoi(N, 'A', 'C', 'B')
