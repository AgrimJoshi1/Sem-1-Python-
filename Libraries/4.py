import pandas as pd 

s1 = pd.Series(["A","B","C"])
s2 = pd.Series(["X","Y","Z"])

df = pd.DataFrame({
    "col1":s1,
    "col2":s2
})

print(df)