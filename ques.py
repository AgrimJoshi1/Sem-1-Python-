# integers = list(map(int, input().split()))
# freq = {}
# subsets = [[]]
# for x in integers:
#     subsets += [s + [x] for s in subsets]
# for s in subsets:
#     if sum(s) % 2 == 0:
#         key = tuple(sorted(s))
#         freq[key] = freq.get(key, 0) + 1

# print("{", end=" ")
# first = True
# for k, v in freq.items():
#     if not first:
#         print(",", end=" ")
#     print(f"{list(k)}:{v}", end=" ")
#     first = False
# print("}")

# integers = list(map(int(int,input().split())))
# n = len(integers)
# output = {} 
# for i in range (n):
#     for j in range(i,n):
#         subset  = integers[i,j+1]
# integers = list(map(int, input().split()))
# n = len(integers)
# output = {}

# for i in range(n):
#     for j in range(i, n):
#         subset = integers[i : j+1]
#         if sum(subset) % 2 == 0:
#             key = tuple(sorted(subset))
#             output[key] = output.get(key, 0) + 1

# print("{", end=" ")
# first = True
# for k in output:
#     if not first:
#         print(",", end=" ")
#     print(f"{list(k)}:{output[k]}", end=" ")
#     first = False
# print("}")
integers = list(map(int, input().split()))
output = {}

subset = []

def generate(i):
    if i == len(integers):
        s = subset[:]
        if sum(s) % 2 == 0:
            key = tuple(sorted(s))
            output[key] = output.get(key, 0) + 1
        return
    subset.append(integers[i])
    generate(i + 1)
    subset.pop()
    generate(i + 1)

generate(0)

print("{", end=" ")
first = True 
for k in output:
    if not first:
        print(",", end=" ")
    print(f"{list(k)}:{output[k]}", end=" ")
    first = False
print("}")

