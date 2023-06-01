import numpy as np
arr=np.arange(0,11)
print(arr)

arr2=2*arr 
print(arr2)
arr3=arr2+arr2       #arr+arr
print(arr3)
#same for substraction and multiplication
#scalars can be added, substracted, multiplied, or divided or powering with the array
arr6=arr/arr #warning issued 0/0 is nan, 1/0 is an infinity
print(arr6)

#np.sqrt(arr), np.exp(arr), np.max(arr), np.min(arr), np.sin(arr)->universal array funtions
