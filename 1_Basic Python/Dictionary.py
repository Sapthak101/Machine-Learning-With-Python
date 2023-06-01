dictionary={'k1':'james', 'k2':'tevez'} #dictionary representation in this a key-value pair is formed
print(dictionary['k1'])
dictionary['k1']='brandon'
print(dictionary)
dictionary2={'k1': 'james', 'k2': [1,2,3,4]}
print(dictionary2)
dictionary3={}
dictionary3['1']='Sapthak'
print(dictionary3)
print(dictionary3['1'])
#or
print(dictionary3.get('1'))

val=input("Enter your choice: ")
print(val)
val=int(val)+123 #the val variable gets typecasted to int type
print(val)
#print(dictionary3['k2'][2]) not possible to access an element inside a dictionary using arbitrary index number
print(dictionary2['k2']) #list [] are represented in the output
#to append a dictionary
#use dict_name.update(arguments)