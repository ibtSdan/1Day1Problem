n = int(input())
for _ in range(n):
    check = True
    inp = input().strip()
    stack = []
    for s in inp:
        if not stack and s==')':
            check = False
            break
        elif s=='(':
            stack.append(s)
        else:
            stack.pop()
    if check and not stack:
        print("YES")
    else:
        print("NO")