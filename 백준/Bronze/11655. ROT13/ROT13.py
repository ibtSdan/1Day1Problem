s = input().rstrip()
res = []

for c in s:
    if 'a' <= c <= 'z':
        res.append(chr((ord(c)-ord('a')+13)%26 + ord('a')))
    elif 'A' <= c <= 'Z':
        res.append(chr((ord(c)-ord('A')+13)%26 + ord('A')))
    else:
        res.append(c)

print(''.join(res))