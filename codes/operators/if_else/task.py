#task
print("----------Enter student details----------")
n=input("Enter name: ")
c=input("Enter class: ")
r=int(input("Enter roll no: "))
print("---Enter marks out of 100---")
eng=float(input("Enter marks in english: "))
hindi=float(input("Enter marks in hindi: "))
sci=float(input("Enter marks in science: "))
sst=float(input("Enter marks in sst: "))
maths=float(input("Enter marks in maths: "))
total=eng+hindi+sci+sst+maths
Per=total*100/500
if Per>90 and Per<100:
    grade="A+"
elif Per>80 and Per<90:
    grade="A"
elif Per>70 and Per<80:
    grade="B+"
elif Per>60 and Per<70:
    grade="B"
elif Per>50 and Per<60:
    grade="C+"
elif Per>40 and Per<50:
    grade="C"
elif Per>33.3 and Per<40:
    grade="Pass"
else:
    grade="Fail"

print("-----Student profile-----")
print("Class:",c)
print("Roll no: ",r)
print("Name: ",n)
print("English: ",eng)
print("Maths: ",maths)
print("Science: ",sci)
print("Sst: ",sst)
print("Total marks: ",total)
print("Percentage: ",Per)
print("Grade: ",grade)
