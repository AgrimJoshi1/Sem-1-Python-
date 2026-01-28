#input 2d list 
#make into dict which will be inputted in list with number as key and freq as value 
mat = []
res = []
n = int(input("number of rows: "))
m = int(input("number of cols: "))
for i in range(n):
    row = []
    for j in range(m):
        n1 = int(input(f"input element of index ({i}, {j}): "))
        row.append(n1)
    mat.append(row)
print(mat)
for i in mat:
    freq = {}
    for num in i:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    res.append(freq)

print(res)