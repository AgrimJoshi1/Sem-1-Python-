
list = []
n = int(input("Enter how many numbers to input: "))
for i in range (1,n+1):
    x = int(input("Enter number to append: "))
    list.append(x)
print(list)
#for even numbers 
list2 = []
print("even numbers are: ")
for x in list: 
    if x%2 == 0: 
        list2.append(x)
        print(list2)


