a = int(input("Enter a number: "))
b = a 
rev = 0 
while a > 0: 
    r = a%10 
    rev = rev * 10 + r 
    a = a//10 

if b == rev: 
    print("Palindrome")
else:
    print("end")
    