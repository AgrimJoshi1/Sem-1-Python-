mat = []
for i in range(3):
    row = []
    for j in range (3):
        n = int(input(f"(n ke elements {i}{j})"))
        row.append(n)
        mat.append(row)
for row in mat: 
    for num in row:
        if num % 2 == 0:
            print(num, end = '')
        print()