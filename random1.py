import random as r 
list = []
print(r.random())
print(r.randint(10,50))
for i in range (0,5):
    x = r.randint(10,100)
    list.append(x)
print(list)