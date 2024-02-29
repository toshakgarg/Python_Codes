#pass or fail
print("Enter marks of students out of 100:")
E=eval(input("enter marks of student in english: "))
M=eval(input("enter marks of student in marks: "))
S=eval(input("enter marks of student in science: "))
Sst=eval(input("enter marks of student in Sst: "))
H=eval(input("enter marks of student in hindi: "))
Per=(E+M+S+Sst+H)/5

if Per>=33.3:
    print("Student is sucessfully pass with",Per)
else:
    print("Student got failed")

    
