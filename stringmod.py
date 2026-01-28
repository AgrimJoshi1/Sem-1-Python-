stri = input("Enter a string: ")
opt = int(input(print('''1. Uppercase 
      2. Lowercase
      3. find index
      4. replace 
      5.find if in string''')))


if(opt==1):
    print(stri.upper())
elif(opt==2):
    print(stri.lower())
elif(opt==3):
    print(stri.find())
elif(opt==4):
    to_rep = input("Enter the string to replace")
    rep = input("Enter the string to replace: ")
    print(stri.replace(to_rep, rep))
elif(opt==5):
    to_find = input("Enter String to find.")
    print(stri.find(to_find))
else:
    print("Thankyou")



