#peledron of number
num=int(input("Enter a numbner: "))
n=num
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse of",n,"is:",rev)
if n==rev:
    print("Number",n," is peledron")
else:
    print("Number",n,"is not peledron")
