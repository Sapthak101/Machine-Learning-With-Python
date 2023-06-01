x=(30, 40, 50) #tuples can be distinguished from list by seeing their enclosing brackets
#a tuple cannot be incrmented or decremented
y=30, 40, 50 #automatically tuple is invoked
a, b, c= 10, 50, 60 #assinging value to a tuple
#tupel can be searched similar to that of the lists
x1=(49, 60)
lista=[x,x1]
print(lista)
tup1=(age, years)='30, 23'.split(',') #segrating a string connected with a comma
print(tup1[0])
tup2=(x,x1)
print(tup2) #tupe output in jupyter and command line are both same
def tupret(a):
    area=a*a
    len=a+20
    return (area, a)
tup3=tupret(8)
print(tup3)
