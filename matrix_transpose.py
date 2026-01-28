mat = []
n = int(input("number of rows"))
m = int(input("number of cols"))
for i in range(n):
    row = []
    for j in range (m):
        n = int(input(f"(input element of index {i} {j}"))
        row.append(n)
    mat.append(row)
print(mat)
transpose= []
for i in range (len(mat)):
    row = []
    for j in range(len(mat[i])):
        row.append(mat[j][i])
    transpose.append(row)
print(transpose)