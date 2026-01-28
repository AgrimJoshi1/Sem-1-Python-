try: 
    li = []
    list_elements = int(input("Enter number of items in list: "))
    for i in range (list_elements):
        x = input(f"Enter {i+1} element: ")
        li.append(x)
    print(li)
    index_in = int(input("Which index element to print: "))
    print(li[index_in])
except (Exception) as e :
    print(f"Error Occurred {e}")
