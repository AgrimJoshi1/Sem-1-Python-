number = int(input("Enter Number to check: "))
c=1
for i in range(2,number):
    if number%i == 0:
        c=0
        print("Not prime")
        break
if(c==1):
        print("prime")