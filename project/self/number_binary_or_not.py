#whole number is bianry or not

num=int(input("enter a number to check binary number: "))
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
    print(n,"is a binary number.")
else:
    print(n,"is not a binary number.")
