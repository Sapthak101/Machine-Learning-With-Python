print(list(range(0, 9, 1)))
print(list(range(9, 0, -1)))
#iterating through a range function
for n in list(range(10, 0, -1)): #converts the range out into a list, eventhough the range by default is a list
    print(n)
x=[0, 1, 4]
for item in range(len(x)): #len(x) means the length of the list x thus it  will iterate through the range set as per its and and item will represent the index
    print(x[item]) #using x[item] the value at a certain position can be printed