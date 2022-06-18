import numpy as np
A=[]       
print("Enter the element ::>")
for i in range(3): 
   row=[]                                      
   for j in range(3): 
      row.append(int(input()))           
   A.append(row)                     
print(A)
print("Display Array In Matrix Form")
for i in range(3):
   for j in range(3):
      print(A[i][j], end=" ")
   print()                                      
B=[]
print("Enter the element ::>")
for i in range (3): 
   row=[]                                      
   for j in range(3): 
      row.append(int(input()))           
   B.append(row)                       
print(B)
print("Display Array In Matrix Form")
for i in range(3):
   for j in range(3):
      print(B[i][j], end=" ")
   print()                                           
result = [] 
result = np.dot(A,B)
print("\nmatrix after addition :\n")
print(result)