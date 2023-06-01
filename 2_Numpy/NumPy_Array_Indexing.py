import numpy as np
arr=np.arange(0,11)
print(arr)
num7=arr[8]
arr2=arr[1:5] #starts from index 1 and upto index 4
print(arr2) #creates an array staring from index 1 to 5
arr3=arr[:6] #elemts from index zero to five
print(arr3)
arr[0:5]=100
print(arr) #broadcasts the position form index 0 upto 4 to 100
arr=np.arange(0,11)
print(arr)
arr4=arr[5:] #represents the elements starting from index 5 up and until the end
print(arr4)
slice_of_array=arr[0:6] #here zero depicts the starting index and 6 depicts the number of elemets to be displayed starting from index 0 
print(slice_of_array)
print(slice_of_array[:])
slice_of_array[:]=99 #the whole array is broadcasted with the value 99
print(slice_of_array)
print(arr) #numpy does not automatically make the copy of a list, instead it sets references to the orginal list
#that means any modifications made in the newly made array will also be reflected to the orginal array
#to make a copy of a list
list_copy=arr.copy()
list_copy[:]=98
print(list_copy)
print(arr)
print(arr[:2])
#indexing a 2D array
arr_2D=np.array([[2,3,4], [5,5,7], [4,8,9]])
print(arr_2D)
print(arr_2D[2]) #returns a whole row from the array
print(arr_2D[0][1]) #returns a element from the array or print(arr_2D[0,1])
#to get a sub matrix from the parent matrix
print(arr_2D[:2])
print(arr_2D[1:])
print(arr_2D[:2,1:])

#logical operation or boolean array
arr6=np.array([1,2,3,4,5,6])
print(arr6)
arr7=arr6>5 #returns an array of boolean values
print(arr7)
#now that resultant arra can be used to create an array where the condition for the array is true
arr8=arr6[arr7]
print(arr8) #respresents an array where the conditio is true
#or 
print(arr6[arr6>2])