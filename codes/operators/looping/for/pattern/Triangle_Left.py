#LFT Triangle
n=int(input("Enter number of column: "))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
