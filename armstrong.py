a = int(input("Enter a number: "))
b = a 
sum = 0 
while a>0:
    r = a%10
    sum = (r**3) + sum 
    a = a//10
if sum == b:
    print("Number is Armstrong.")
else: 
    print("end")