#Reverse of number
num=int(input("Enter a number for reverse: "))
n=num
rev=0
#condition in looping
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("Reverse of",n,"is:",rev)
