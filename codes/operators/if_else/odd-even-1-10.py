#odd even(1-10)
for i in range(12):
    a=int(input("Enter a number with in 1-10: "))

    if a==0 or a==2 or a==4 or a==6 or a==8 or a==10:
        print("even number")

    elif a==1 or a==3 or a==5 or a==7 or a==9:
        print("odd number")

    else:
        print("!ERROR, Invalid entry")
        print(a,"is not between 0-10")
