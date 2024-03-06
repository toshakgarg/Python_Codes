#RAT 2 num Vertical
n=int(input("Enter no of rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
