#sum and average of m natural number
n=int(input("Enter number upto calculate sum and average: "))
sm=0
i=1
while i<=n:
    sm=sm+i
    i=i+1
print("Sum of",n,"natural number",sm)
av=sm/n
print("Average of",n,"natural number is",av)
