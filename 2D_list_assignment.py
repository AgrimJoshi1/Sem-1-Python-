R = int(input())
matrix = []
for i in range(R):
    line = input().strip()
    if line == "":
        matrix.append([])
    else:
        matrix.append(list(map(int, line.split())))
print(matrix)
total = sum(len(row) for row in matrix)


dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0  

