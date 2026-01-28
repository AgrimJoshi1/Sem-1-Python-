n = int(input("Enter a number: "))
c = 1
for i in range(1,n+1):
    for j in range(i,i+i):
        print(c, end = ' ')
        c = c+1
    print()
