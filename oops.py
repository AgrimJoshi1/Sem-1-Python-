# class student:            #class, class ke andar def is methods
#     name = 'ABC' #attributes
#     grade = 10 

# s1 = student()
# print(s1.name, s1.grade)

# s2 = student()


#class attributes are shared by all the elements of the class 
#instance attributes are made for an instance value for every object will change

'''class student: 
    def __init__(self,fname,cgrade):    
        self.name = fname 
        self.grade = cgrade
s1 = student('ABC',10)
print(s1.name,s1.grade)
s2 = student('XYZ',20)
print(s2.name,s2.grade)
'''    

# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name=name
#         self.grade=grade
#         self.percentage=percentage

#     def display(self):
#         if self.percentage>80:
            
#             print(f"{self.name} is in class {self.grade} with grade A")
#         elif self.percentage>60 and self.percentage<40:
#             print(f"{self.name} is in class {self.grade} with grade B")
#         else:
#             print(f"{self.name} is in class {self.grade} with grade C")


# s1=Student('ABC',10,96)
# s2=Student('cDE',10,49)

# s1.display()
# s2.display()

#2 type classes 
#2yper methods 
#2 type attributes


'''class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def display(self):
        print(f"{self.name} is in class {self.grade}")
s1=student("ABC",10)
s1.display()         
class Graduation(student):
    def __init__(self,name,grade,stream):
        super().__init__(name,grade)
        self.stream=stream
    def display(self):
        super().display
        print(f"stream is {self.stream}")
g1=Graduation("abc",10,"CSE")
g1.display()
'''

class account:
    def __init__(self, bank_name, account_no, limit):
        self.bank_name = bank_name
        self.account_no = account_no
        self.limit = limit


class Saving(account):
    def __init__(self, bank_name, account_no, limit):
        super().__init__(bank_name, account_no, limit)

    def check_saving(self):
        if self.limit >= 50000:
            print("Saving Account Approved")
        else:
            print("Saving Account Not Approved")


bank_name = input("Enter bank : ")
account_no = int(input("Enter account: "))
limit = float(input("Enter limit: "))

s = Saving(bank_name, account_no, limit)
s.check_saving()

