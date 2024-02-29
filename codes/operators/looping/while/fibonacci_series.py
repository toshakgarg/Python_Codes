#Fibonacci series
n=int(input())
a=0
b=1
i=1
while i<=n:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)
