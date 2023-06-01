num1=5
num2=7
print(num1>num2 and num1<num2)
print(num1>num2 or num1<num2 or num1!=num2) #two or more comparisons
print(not num1>num2) #takes a single comparison
#NOT-AND-OR (Order of Evaluation)
print(False or not True and True)
result=(False or (not True)) and True
print("The result is", result, num1) #to print predetermined values
#identity operators
result=5 is 6
print(result)
result=5 is not 6
print(result)