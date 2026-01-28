#remove duplicates from list 

l1 = [1,2,3,4,5,6,7,2,3,3,4,4,5,6,7]
d1 = []
for i in l1:
    if i not in d1:
         d1.append(i)

print(d1)

