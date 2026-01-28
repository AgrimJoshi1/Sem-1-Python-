x={"abc":"123","xyz":"tfd"}
print(x)
x.pop("abc")
print(x)
x.clear()
print(x)
for i in x:
    print([i])