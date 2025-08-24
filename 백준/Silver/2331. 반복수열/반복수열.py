a, p = map(int,input().split())
lst = [a]
idx = 1
while True:
    n = 0
    for s in str(lst[idx-1]):
        n += int(s)**p
    if n in lst:
        print(len(lst[:lst.index(n)]))
        break
    else:
        lst.append(n)
        idx += 1