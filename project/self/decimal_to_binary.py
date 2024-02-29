num=int(input("Enter a number: "))
n=num
bno=0
while num!=0:
    rem=num%16
    bno=bno*10+rem
    num=num//16
print("Binary number of",n,"is:",bno)
