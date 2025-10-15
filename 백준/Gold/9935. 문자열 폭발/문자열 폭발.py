s = input().strip()
boom = input().strip()
n = len(boom)

ans = []
for c in s:
    ans.append(c)
    if len(ans)>=n and ''.join(ans[-n:])==boom:
        del ans[-n:]


ans = ''.join(ans)
print(ans if ans else "FRULA")