dict = {}
dict_new = {}
num_entries = int(input("Enter the number of key-value pairs: "))


for i in range(num_entries):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict[key] = value
key_check = input("Enter the key to check: ")

if key_check in dict: 
    dict_new[key_check] = value
    print("New Dictionary Created:" , dict_new)
else: 
    print("not in dict")



