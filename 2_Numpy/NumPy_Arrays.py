my_list=[1,2,3]
print(my_list)
print(my_list[0])
import numpy as np
arr=np.array(my_list) #converting the list ijtop an array
print(arr)
print(arr[0])
my_mat=[[1,2,3],[4,5,6]] #list of lists
print(my_mat)
arr2=np.array(my_mat) #casting the list of list into an numpy array, and thus it is converted into a two dimensional array
print(arr2)
print(arr2[0])
print(arr2[0][1])
#my_mat2=np.array(listc=["Sapthak", 1, "James"]) heterogeneous data cannot be stored in an array
#print(my_mat)
#creating a numpy array using np.arrange()funtion
arr4=np.arange(0,10)  #same as python range funtion it will create an array containing 10 intgers evenly spaced the first value is the stater annd the second value is the before end value and the last one is the step value
print(arr4)
arr5=np.arange(0,10,2)
print(arr5)
 #making an array of all zeros
arr6=np.zeros(3) #argument is the number of zeros to be created
print(arr6)
arr7=np.zeros((5,5)) #creating a 2D array of all zeros by giving a tuple as an input
print(arr7)
arr7=np.ones((3,4))
print(arr7)
arr8=np.linspace(0,5,10)  #returns an array of 10 evenly spaced points from 0 to 5
print(arr8)
arr9=np.eye(5) #prints the number of ones equal to that of the argument indity matrix
print(arr9)

arr10=np.random.rand(5) #creating an array of 5 elememts with an uniform distribution between 0 and 1, random object and its method
print(arr10)
arr11=np.random.rand(5,5) #on tuple insertion
print(arr11)
arr12=np.random.randn(4,4) #creating an array of 4x4 form a Gausian and Normal distrubution
print(arr12)

randnum=np.random.randint(1, 100) #picking a random integer between two numbers, inclusive at the lowend and exclusive at the high end
print(randnum)

arr13=np.random.randint(1,100,(5,5)) # tuple to create 2D vector or a single input to create a 1D vector
print(arr13)


arr14=np.arange(25)
#print(arr14.reshape(5,4)) to reshape an array numbers of elements should match
print(arr14.reshape(5,5))

max=arr14.max() # to get the max and the min value
min=arr14.min()
index=arr14.argmax() #to get the index of the max value
index2=arr14.argmin()

#to find the shape of a matrix
shap=arr.shape
#resize and array
#arr15=arr14.reshape(5,4)
arr15=arr14.reshape(5,5) #as the array is an object of the library numpy and reshape is one of its funtion
print(arr15)

#to see the datatype of the elements in the array
arr15.dtype 

#from numpy.random import randint, numpy isthe library and random is the object of a class in the library under it the randlint is the method
#to import only a funtion
#and that function can be used without calling the random object
#random(2,10) 
print(type(np.random)) #belongs to the class module, by defualt objects can be accessed directly without reffering to the library
print(type(np.random.randint))