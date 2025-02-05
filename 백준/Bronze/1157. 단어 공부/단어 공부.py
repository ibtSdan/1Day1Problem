s = input().upper()
s_set = list(set(s))
lst = []

for i in s_set:
  lst.append(s.count(i))

print("?" if lst.count(max(lst))>1 else s_set[lst.index(max(lst))])