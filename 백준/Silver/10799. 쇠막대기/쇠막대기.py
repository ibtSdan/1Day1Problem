s = input().strip()
stack = []
ans = 0
for i in range(len(s)):
    if s[i]=='(':
        stack.append('(')
    else:
        stack.pop()
        if s[i-1]=='(':
            ans += len(stack)
        else:
            ans += 1
print(ans)