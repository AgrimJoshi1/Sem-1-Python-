matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

valid_set = {1, 2, 3, 4, 5}
is_sudoku = True

for row in matrix:
    if set(row) != valid_set:
        is_sudoku = False
        break

if is_sudoku:
    for c in range(5):
        col = [matrix[r][c] for r in range(5)]
        if set(col) != valid_set:
            is_sudoku = False
            break

if is_sudoku:
    print("this is sudoku")
else:
    print("not sudoku")
