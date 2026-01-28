employee_type = int(input("1.private or 2.govt: " ))
salary = int(input("Enter salary: "))
exp = int(input("How many YOE? "))
credit_score =int(input("Enter Credit Score: "))

if employee_type == 2:
    if salary >= 50000 and exp>= 2 and credit_score > 700:
        print("Eligible for loan")
    else:
        print("not eligible")
elif  employee_type ==1: 
    if salary >= 50000 or exp>= 2 or credit_score > 700:
        print("Eligible for loan")
    else: 
        print("not eligible")


        

