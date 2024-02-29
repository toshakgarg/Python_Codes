#arnstrong
num=int(input("Enter a numbner: "))
n=num
sm=0
while num!=0:
    rem=num%10
    sm=sm+rem*rem*rem
    num=num//10
if n==sm:
    print("number",n,"is arnstrong")
else:
    print("number",n,"is not arnstrong")
