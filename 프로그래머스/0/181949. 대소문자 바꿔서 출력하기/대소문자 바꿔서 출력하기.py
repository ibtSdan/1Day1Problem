str = input()
ans = []
for s in str:
    if s.isupper():
        ans.append(s.lower())
    else:
        ans.append(s.upper())
print(''.join(ans))