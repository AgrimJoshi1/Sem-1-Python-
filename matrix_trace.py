mat = []
n = int(input("number of rows: "))
m = int(input("number of cols: "))
for i in range(n):
    row = []
    for j in range(m):
        n1 = int(input(f"input element of index ({i}, {j}): "))
        row.append(n1)
    mat.append(row)
print(mat)
sum = 0
for i in range(min(n, m)):
    sum += mat[i][i]
print(f"Trace = {sum}")
