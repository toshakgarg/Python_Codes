#RAT 2
n=int(input("Enter number of rows: "))
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
