import sys
o = input().strip()
if o=='0':
    print(0)
    sys.exit()
ans = []
for s in o:
    s = int(s)
    lst = []
    while s>0:
        n = s%2
        lst.append(n)
        s //= 2
    while len(lst)!=3:
        lst.append(0)
    ans.extend(lst[::-1])
print(''.join(map(str, ans)).lstrip('0'))