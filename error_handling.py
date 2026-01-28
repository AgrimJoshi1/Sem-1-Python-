try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter number 2 : "))
    print(num1/num2)
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError: 
    print("Enter integers only")