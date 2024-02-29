#Electric bill
#Input reading.
nr=int(input("Enter new reading: "))
olr=int(input("Enter old reading: "))

#Calculating unit consumed
uc=nr-olr

#Condition
if uc<100:
    amt=uc*2

elif uc>=100 and uc<300:
    amt=uc*3

elif uc>=300 and uc<500:
    amt=uc*4

elif uc>=500 and uc<800:
    amt=uc*5

else:
    amt=uc*6

#Result
print("Amount of",uc,"is=",amt)
