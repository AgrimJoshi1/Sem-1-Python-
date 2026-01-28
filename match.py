x = input("Enter to check: ")
match x:
    case a if 'a' <= x <= 'z':
        print("This belongs to small letters")
    case a if 'A'<= x<= 'Z': 
        print("This belongs to capital letters")
    case a if '1'<= x <= '9': 
        print("This belongs to digits")
    case _: 
        print("Special Characters")

# check = input("Enter to check: ")
# if 'a'<= check <='z':
#     print("It belongs to small characters.")
# elif 'A'<=check<='Z':
#     print("It belongs to Capital")
# elif check :
#     print("Belongs to digits")
# else:
#     print("Special Characters")
