# random library commands
# 1) random() = gives a random variable in float between 0 & 1
# 2) randint() = gives a random variable in int
# 3) sample() = generates random integers in a list
# 4) choice() = gnerates no from list
# 5) randrange() = takes random till a range specified as start
# 6) uniform() = takes random in float till a range specified as start
# 7) shuffle() = shuffles a list
# 8) seed() = changes the value of seed
import random
'''n = random.random()
print(n)

y = random.randint(10,100)
print(y)

lst =[]
for i in range (5):
    n = random.randint(10,50)
    lst.append(n)
print(lst)

x = random.sample(range(10,50),5)
print(x)

list = [10,20,30,40,50,60]
r = random.choice(list)
print(r)'''

val = int(input("Enter Seed: "))
random.seed(val)
for i in range (10):
    print(random.random())