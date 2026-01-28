dict = {}
dict_new = {}
num_entries = int(input("Enter the number of key-value pairs: "))

for i in range(num_entries):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    dict[key] = value


dict_new[max(dict)] = value

print("dictionary: ", dict)
print(dict_new)