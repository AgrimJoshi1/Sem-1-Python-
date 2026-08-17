import pandas as pd

s1 = pd.Series(["A","B","C"])
s2 = pd.Series(["X","Y","Z"])

ind = [6,7,8]
col = ["col1","col2"]

df = pd.DataFrame(zip(s1,s2),columns = col, index = ind)
print(df)