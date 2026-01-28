r1 = int(input("Enter rows for Matrix 1: "))
c1 = int(input("Enter columns for Matrix 1: "))
r2 = int(input("Enter rows for Matrix 2: "))
c2 = int(input("Enter columns for Matrix 2: "))

print("\nEnter elements for Matrix 1 row-wise:")
m1 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(r1)]

print("\nEnter elements for Matrix 2 row-wise:")
m2 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(r2)]

print("\nMatrix 1:", m1)
print("Matrix 2:", m2)

print(m1,m2)
m3 = []
for i in range(r1):
    row = []
    for j in range(c1):
        row.append(m1[i][j] + m2[i][j])
    m3.append(row)

print("Resultant matrix after addition (m3):")
for row in m3:
    print(row)