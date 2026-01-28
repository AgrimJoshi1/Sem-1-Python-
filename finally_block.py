# try:
#     num1 = int(input())
#     num2 = int(input())
#     num3 = num1/num2
#     while num3 != int:
#         print("attempt done")
#     else: 
#         print(num3)
# except Exception: 
#     print("Erroror")
# finally:
#     print("Attempt done")


# num = int(input("enter numbers: "))
# num2 = int(input("enter numbers: "))
# while num >0:
#     try:
        
#         if num%num2 ==0:
#             num = num/num2
#             print(num)
#         else:
#             break
#     except ZeroDivisionError:
#         print("error occured")



while True: 
    try: 
    a = int(input("no.")) 
    b = int(input("no.")) 
    res = a/b
    print(res)
    break
    except ZeroDivisionError: 
        print("cannot divide by zero")
    except ValueError: 
        print("int only")
    finally: 
        print("Attempt done")