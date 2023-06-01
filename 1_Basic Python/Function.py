def simple():
    name1="Sapthak" 
    name2="Mohajon"
    print(f"Hello {name1}, {name2}") #f string usage
simple()

def plus_ten(a): #parameters present
    return (a+10)

print(plus_ten(20)) #arguments given

def wage(a):
    return (50*a)
def wageplus(a):
    return (wage(a)+50)
print(wageplus(8))
#in python we can also use multuple arguments within the function
#built in function max() return the highest value, min() returns the lowest value

lista={1, 2, 4, 5} #list can also store strings and they can be referenced with index numbers
print(abs(-10))
print(sum(lista)) #in sum a list can be passed as an argument
print(round(3.55, 2)) #rounds to 2 decimal places
print(round(3.55)) #rounds to the next possible integer
print(pow(2, 4))
print(len("sapthak"))
print(len(lista)) #it can be used to find the number of argumeent in a list or in a word
listb={"Sapthak", "James", "Rice"}
#print(sum(listb)) in sum funtion strings can not be used as an argument
print(len(1,2,4,5))#len function can take only one argument, a character or a string or a list have n elements
#in python default values within the function name can also be used
# like c++
# if a dictionary is passed as an argument in the python funtion and its value under a certain key is changed it also be reflected outside because dictionaries are mutable
# in a function if nothing is passed inside a funtion (but still it a paramter attached) without defaulterizing it 
# then then false as an agrument can be used while calling the function
# funtions can also be nested it its usage is not needed in the outside