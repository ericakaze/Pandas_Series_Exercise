import numpy as np 
import pandas as pd 

elements= np.random.randint(0, 101, 20)
elements_Series= pd.Series(elements)
print(elements_Series)
elements_statistics=elements_Series.describe()
print(elements_statistics)
