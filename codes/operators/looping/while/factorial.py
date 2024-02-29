#factorial fo number
x=int(input("Enter a number for factorial: "))
fac=1
i=x
while i>=1:
    fac=fac*i
    i=i-1
print("Factorial of",x,"is:",fac)
