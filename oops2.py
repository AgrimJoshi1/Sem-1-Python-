#you have to create a class mobile and make 2 objects storing the value brand and price of the mobile
class mobile: 
    def __init__(self,brand,price):
        self.price = price 
        self.brand = brand 
    def display(self):
        print(f"{self.brand} it costs {self.price}")
m1 = mobile('samsung',20000)
m2 = mobile('apple',60000)
#mobile.display()
    
    

print(m1.brand, m1.price)
print(m2.brand, m2.price)