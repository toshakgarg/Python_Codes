#RAT 2 num horizontal
n=int(input("Enter number of Rows: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
