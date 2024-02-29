#grade to student
print("Enter marks of students out of 100:")
E=eval(input("enter marks of student in english: "))
M=eval(input("enter marks of student in marks: "))
S=eval(input("enter marks of student in science: "))
Sst=eval(input("enter marks of student in Sst: "))
H=eval(input("enter marks of student in hindi: "))
Per=(E+M+S+Sst+H)/5

if Per>90 and Per<100:
    print("student is pass with A+ grade")
elif Per>80 and Per<90:
    print("Student is pass with A grade")
elif Per>70 and Per<80:
    print("Student is pass with B+ grade")
elif Per>60 and Per<70:
    print("Student is pass with B grade")
elif Per>50 and Per<60:
    print("Student is pass with C+ grade")
elif Per>40 and Per<50:
    print("Student is pass with C grade")
elif Per>33.3 and Per<40:
    print("Student is pass")
else:
    print("FAIL")
