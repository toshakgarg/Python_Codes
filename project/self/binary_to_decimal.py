def binary_to_decimal(bno):
    num=0
    i=0
    while bno!=0:
        rem=bno%10
        num=num+(rem*(2**i))
        bno=bno//10
        i=i+1
    print(num)

num=int(input("enter a number: "))
n=num
rev=0
while num!=0:
    rem=num%10
    if rem==0 or rem==1:
        #it continues the loop upto non-binary digit.
        num=num//10
    else:
        break
        #it break loop at non binary digit.
if num==0:
    binary_to_decimal(n)
else:
    print("\t\t\tERROR! INVALID ENTRY\n",n,"is not a binary number.")
