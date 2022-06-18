import numpy as np
print("first number : ")
x=int(input())
print("second number : ")
y=int(input())
arr=[]
for i in range(x,y+1):
    arr.append(i)
print(arr)
print(len(arr))
z = 6
arr1 = np.zeros(len(arr) + (len(arr)-1)*(z))
for a in range(len(arr)):
    arr1[::z] = arr
print(arr1)