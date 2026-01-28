# #Length of each row and total no of elts in matrix
# l1=[]
# rows=int(input("no of rows"))
# for i in range(rows):
#     row=[]
#     m=int(input(f"enter no of cols in {i+1} row"))
#     for j in range(m):
#         k=int(input(f"Enter elt {i}{j}"))
#         row.append(k)
#     l1.append(row)
# print(l1)
# print("\nJagged List:")
# for row in l1:
#     print(row)
# print("\nLength of each row:")
# for i, row in enumerate(l1):
#     print(f"Row {i+1} length: {len(row)}")
# total_elements = sum(len(row) for row in l1)
# print(f"\nTotal number of elements in matrix: {total_elements}")







    

t1 = (3,4,5,6)
y = list(t1)
y[2]=30
y.append(7)
x = tuple(y)
print(x)