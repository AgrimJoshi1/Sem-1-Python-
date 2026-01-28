#2d list input and pass it to function and return only diagonal elements from that func 
def diag_elem(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    return diagonal

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)

print("The 2D list is:")
for row in matrix:
    print(row)

diagonal = diag_elem(matrix)
print("diagonal elements are", diagonal)
