#creating matrix A,B,C
row,coll=(3,3)
a=[[ 0 for i in range(coll)] for j in range(row)]
b=[[ 0 for i in range(coll)] for j in range(row)]
c=[[ 0 for i in range(coll)] for j in range(row)]  
#Updating matrix(A)
a[0][0]=1
a[0][1]=2
a[0][2]=3
a[1][0]=4
a[1][1]=5
a[1][2]=6
a[2][0]=7
a[2][1]=8
a[2][2]=9
#Printing updated matrix(A)
print("Element of matrix are:")
for i in range(3):
  for j in range(3):
    print(a[i][j],end=" ")
  print()


#applying opperation on martix(A) for adjoint and save in matrix(B)
b[0][0]=(a[0][0])*        ((a[1][1]*a[2][2])-(a[2][1]*a[1][2]))
b[0][1]=(-1)*(a[0][1])*   ((a[1][0]*a[2][2])-(a[2][0]*a[1][2]))
b[0][2]=(a[0][2])*        ((a[1][0]*a[2][1])-(a[2][0]*a[1][1]))

b[1][0]=(-1)*(a[1][0])*   ((a[0][1]*a[2][2])-(a[2][1]*a[0][2]))
b[1][1]=(a[1][1])*        ((a[0][0]*a[2][2])-(a[2][0]*a[0][2]))
b[1][2]=(-1)*(a[1][2])*   ((a[0][0]*a[2][1])-(a[2][0]*a[0][1]))

b[2][0]=(a[2][0])*        ((a[0][1]*a[1][2])-(a[1][1]*a[0][2]))
b[2][1]=(-1)*(a[2][1])*   ((a[0][0]*a[1][2])-(a[1][0]*a[0][2]))
b[2][2]=(a[2][2])*        ((a[0][0]*a[1][1])-(a[1][0]*a[0][1]))
#printing adjoint of matrix(A) in form of matrix(B)
print("Adjoint of matrix without looping is:")
for i in range(3):
  for j in range(3):
    print(b[i][j],end="  ")
  print()


#applying loop for adjoint of matrix(A) and save in matrix(C)
for i in range(3):
  for j in range(3):
    #condition for collumn
    if j==0:
      r=1
    else:
      r=0
    if j==2:
      t=1
    else:
      t=2
    #condition for row
    if i==0:
      s=1
    else:
      s=0
    if i==2:
      k=1
    else:
      k=2
      
    #formula of adjoint
    c[i][j]=(a[i][j])*((a[s][r]*a[k][t])-(a[k][r]*a[s][t]))
    #conditon for (-ve) sing
    if (i+j+2)%2!=0:
      c[i][j]=c[i][j]*(-1)
print("Adjoint of matrix with looping is:")
for i in range(3):
  for j in range(3):
    print(c[i][j],end="  ")
  print()

