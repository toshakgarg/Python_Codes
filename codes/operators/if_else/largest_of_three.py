#largest of three
print("enter three number")
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))

if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
elif c>a and c>b:
    print("c is largest")
else:
    print("!ERROR, invalid numbers")
