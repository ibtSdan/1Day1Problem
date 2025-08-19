string = input().strip()
lst = []
for i in range(len(string)):
    lst.append(string[i:])
lst.sort()
for s in lst:
    print(s)