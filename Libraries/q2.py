#mean, greater than mean
import pandas as pd


l1 = list(map(int,input().split()))

s1 = pd.Series(l1)

mean = s1.mean()

c = 0
for i in l1:
    if i>mean:
        c+=1

print(mean)
print(c)

