n = int(input("Enter number of sets: "))
l1 = []

for i in range(n):
    x = input(f"Enter set for set {i+1} : ")
    e = set(x.split())
    l1.append(e)

set = set()
for s in l1:
    set.update(s)

list_ele = list(set)
count_list = []

for elt in list_ele:
    count = 0
    for s in l1:
        if elt in s:
            count += 1
    count_list.append(count)

max_count = max(count_list)
max_elts = [list_ele[i] for i in range(len(list_ele)) if count_list[i] == max_count]

print("List of sets:")
for idx, s in enumerate(l1, 1):
    print(f"Set {idx}: {s}")

print(f"\n({max_count} ): {set(max_elts)}")