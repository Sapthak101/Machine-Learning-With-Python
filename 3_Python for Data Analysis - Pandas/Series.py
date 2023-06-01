import numpy as np
import pandas as pd
 
labels=['a', 10, 'c'] #[a', 'b', 'c']
my_data=[10, 20, 30]
arr=np.array(my_data)
d={'a':10, 'b': 20, 'c':30}

print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels))
print(pd.Series(my_data, labels))
#difference bewteen series and dictionaries is that a dictionary can store heterogeneous data and index
#but Series can store homogeneous data and heterogenoous labels 
pd.Series(arr) #passing a numpy array
pd.Series(arr, labels) #passing a numpy array with the labels
pd.Series(d) #passing a dictionary with the correct datatype ordering
pd.Series(data=labels)
print(pd.Series(data=[sum, print, len])) #cannot be done with the numpy array
ser1=pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
