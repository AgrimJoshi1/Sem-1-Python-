quantity = int(input("Enter value you want to purchase:"))
if quantity>1000: 
    raise ValueError('Stock Limited to 1000 only')
else: 
    print('Stock booked')