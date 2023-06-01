# a module is a collection of funtion and class definitions
# a package=library is a collection of modules
# a standard library is a collection of modules available as soon as python is installed
# Examples .extend()=method, len()=funtions
# using modules
import math
num=2
num2=math.sqrt(num)
print(num2)
print(math.sqrt)

# or
from math import sqrt
num3=sqrt(16)
print(num3)

# or renaming sqrt funtion
print(sqrt)

from math import sqrt as s
num4=s(78)
print(num4)

# renaming the math module name
import math as m
num5=m.sqrt(16)
print(num5)

# to import all the modules from a package
# the drawback of this is that if a second package uses the same funtion for a different purpose then conflict may occur
#syntactical conflicts like sqrt() etc
from math import *
num6=math.sqrt(18)
num7=sqrt(18)
print(num6)
print(num7)