data=["Sapthak", "Ayman", "Jaffar", 'James'] #obs within the list the string items can be represented by using a single quotation or a double quotation
print(data[0]) #to extract an item from a list
print(data[0][1])#to extract the character from an item
print(data[-1])#to extract an item from the back
data[3]='Austin' #to replace an item in the list or within ""
# a list can be of number or characters or strings
print(data)#to print the whole list or in Jupyter just type data
del data[2]#deletes an element in the list and due to that the whole index system in the list gets modified
print(data)
data.append("David")# to append a list as data is a object and belonging to it the method append is introduced and it takes only one argument
print(data)
data.extend(["curtis", 'jadon']) #to extend a list here also a singla argument is passed and which is a sublist appende to the main list
print(data)
print("The first item in the list"+ data[1])#list items are automatically treated as a string but not in case if numbers a re stored
listc=[2,1,3,4,5]
print("The number in the list "+str(listc[2]))
print(len(listc))
print(len("Sapthak"))
#list slicing
print(data[1:3])
print(data)
listd=data[1:3]
print(listd)
data[:2]#0 to 2 slice
data[2:]#from 2 till the end of the last item inthe list
data[-2:]
print(data.index("Austin"))#to know the the postion of an item in the list
#concatenating two lists
liste=[data, listc]
print(liste)#list within a list
data.extend(liste)#to extend a lsit using another list
print(data)
listc.sort()#to sort a lsit
print(listc)
listc.sort(reverse=True)#arranging a list in reverse order
print(listc)

def split(phrase):
    word=phrase.split(' ')
    print(word)
split("I am Sapthak")