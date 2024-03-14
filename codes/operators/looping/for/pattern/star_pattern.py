for j in range(6):
    for k in range(-8,6-j):
        print(" ",end="")
    for l in range(0,2*j-1):
        print("*",end="")
    print()
for m in range(11,0,-1):
    for n in range(-2,12-m):
        print(" ",end="")
    for o in range(2*m-1):
        print("*",end="")
    print()
    if m==9:
        break
for i in range(4):
    for j in range(-2,4-i):
        print(" ",end="")
    for k in range(15+2*i):
        print("*",end="")
    print()
for j in range(5,0,-1):
    for k in range(6-j,-8,-1):
        print(" ",end="")
    for l in range(2*j-1,0,-1):
        print("*",end="")
    print()
