grid = []
for i in range(3):
    grid.append([" "] * 3)  

while True:
    print("\nCurrent board:")
    for row in grid:
        print(row)

    choice = input("\nDo you want to place a move? (yes/no): ").lower()
    if choice == "no":
        break

    row = int(input("Enter row (1-3): ")) - 1
    col = int(input("Enter column (1-3): ")) - 1

    if row not in range(3) or col not in range(3):
        print("Invalid position! Try again.")
        continue

    if grid[row][col] != " ":
        print("Position already used! Choose another one.")
    else:
        grid[row][col] = "X" 
        print("Move placed!")

print("\nFinal board:")
for row in grid:
    print(row)

n = len(grid)
rotated = [[0]*n for _ in range(n)]


for r in range(n):
    for c in range(n):
        rotated[r][c] = grid[n - 1 - c][r]
for row in rotated:
    print("rotated row" ,row)
