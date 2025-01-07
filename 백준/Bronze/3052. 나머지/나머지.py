lst = []
for _ in range(10):
    lst.append((int(input()))%42)
s = set(lst)
print(len(s))