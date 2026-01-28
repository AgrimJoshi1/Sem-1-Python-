num1 = float(input("Enter First Number: "))
num2= float(input("Enter Second Number: "))

print("1. Additing" \
"      2. Subbtraction" \
"      3. Multiplication " \
"      4. Division")
opr = int(input("Enter the number corresponding to the operation: "))

if(opr ==1): 
    print(num1 + num2)
elif(opr==2):
    print(num1 - num2)
elif(opr==3):
    print(num1*num2)
elif(opr==4): 
    print(num1/num2)
else: 
    print("Error")

