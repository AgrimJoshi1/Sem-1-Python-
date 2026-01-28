'''5*5 empty matrix, ask the user to occupy one seat, update the matrix, if same place is asked to occupy show message that the seat
is occupied, keep on updating, at last print the occupied seats represented by 1 and unoccupied as - '''
matrix = []
for i in range(5): 
    matrix.append(["0"] * 5)

while True:
    print("unoccupied matrix:")
    for row in matrix:
        print(row)
    choice1 = int(input())
    choice = input("\nDo you want to occupy a seat? (yes/no): ").lower()
    if choice == "no":
        break
    row = int(input("Enter row : ")) - 1
    col = int(input("Enter column: ")) - 1
 
    if row not in range(5) or col not in range(5):
        print("Invalid seat position! Try again.")
        continue

    if matrix[row][col] == 1:
        print("Seat already occupied, Choose another one:")
    else:
        matrix[row][col] = 1
        print("Occupied")

print("Seats: ")
for row in matrix:
    print(row)
