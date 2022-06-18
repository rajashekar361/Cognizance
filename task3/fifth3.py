import numpy as np
n=int(input("enter the size of identity matrix: "))
a=np.identity(n)
print("identity matrix of ",n )
print(a)
m=int(input("enter the any another size of identity matrix:"))
b=np.identity(m)
print("identity matrix of ",m )
print(b)