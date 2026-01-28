list = []
#input number of sets in the list 
set_count = int(input("Enter number of sets: "))


for i in range(set_count):
    x = input(f'Enter elements for set:  {i + 1}')
    set_in = set(x.split())
    list.append(x)
for i in range (set_count):
    list
                
print(list)
 
print(y)



# from functools import reduce
# list = []
# #input number of sets in the list 
# set_count = int(input("Enter number of sets: "))


# for i in range(set_count):
#    m = set(map(int, input("Enter elements of first set : ").split()))
#    list.append(m)
# print(list)    
# def inter (a,b):
#     return a.difference(b)

# s2= reduce(inter,list)
# print(s2)

