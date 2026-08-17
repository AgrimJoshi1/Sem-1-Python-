import pandas as pd 

#1D series 2D dataframe

l1 = [1,2,3,4]
ind = ["helo","bye","tata","byebye"]

s = pd.Series(l1, index = ind)

print(s)