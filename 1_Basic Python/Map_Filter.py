numbers=[1,2,3]

def double(a):
    return (a*2)

result=map(double, numbers) #while using map the function call inside the map function is passed by only using its name 
print(list(result)) #similar to range

#or
number1=[3,4,5]
result=map(lambda a : a *2, number1)

#filtering results

result2=filter(lambda a:(a%2==0), numbers) #body in the form of lambda funtion can also be passed
print(list(result2))