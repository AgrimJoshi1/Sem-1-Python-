#Range (25% - 1.5*W)
#(q1 - 1.5*w)

import pandas as pd

l1 = list(map(int,input().split()))

q1 = pd.Series(l1).quantile(0.25)
q2 = pd.Series(l1).quantile(0.75)

w = q2-q1
lower = q1 - 1.5*w
higher = q1 + 1.5*w

for i in l1:
    if i>higher or i<lower:
        c+=1

print(c)
print(len(l1)-c)


