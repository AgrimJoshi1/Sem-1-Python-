mat = []
n = int(input("number of rows"))
for i in range(n):
    row = []
    m = int(input(f"enter number of cols in {i + 1} row: "))
    for j in range (m):
        k = int(input(f"enter element, {i} {j}: "))
        row.append(k)
    mat.append(row)
    print(sum(row))
print(mat)
print(sum(mat))