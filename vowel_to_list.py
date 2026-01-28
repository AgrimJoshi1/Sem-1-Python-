
# li = []
# a = input("Enter a string: ")
# vowels = ['a','e','i','o','u']
# a.join(li)
# for i 
# list = [[1,2,3], [4], [5,6]]
# l1 = []
# for i in list: 
#     for k in range (3):
#         if k < len(i):
#             y = sum(list[k])
#         l1.append(y)

# print(l1)

mat = [[1,2,3], [4], [5,6]]
for i in range(3):
    res = sum(row[i] for row in mat if i <len(row))

print(res)