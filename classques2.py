def diagonal_cube(matrix):
    for i in range(len(matrix)):
        matrix[i][i] = matrix[i][i] ** 3
    return matrix


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

print("2d list:")
for row in matrix:
    print(row)

updated_matrix = diagonal_cube(matrix)

print("updated:")
for row in updated_matrix:
    print(row)
