import pandas as pd

l1 = list(map(int,input().split()))
s = pd.Series(l1)
mean = s.mean()
mode = s.mode()
median = s.median()

print(round(mean,2))
print(f"{mean:.2f}")

#mean, median, modde