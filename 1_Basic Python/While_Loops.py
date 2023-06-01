x=0
while (x<=20):
    print(x)
    x=x+1 # / x+=1
#range(start, stop, step)
#range in python represents a mandatory start value which is incemented by the step value and a stop value that is where to stop
#stop value is equal to the last value printed+1
#the stop value is the most important suppose in range(10) the stop value is 10 and the start value is assumed to be 0, and step value is 1 
range(10, 0, 1)
print(list(range(0, 9, 1)))
print(list(range(9, 0, -1)))