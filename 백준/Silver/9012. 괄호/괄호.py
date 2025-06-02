n = int(input())
for _ in range(n):
    s = input().strip()
    stack = []
    check = True
    for j in s:
        if j=='(':
            stack.append(j)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                check = False
                break
    if stack and check:
        print("NO")
    elif check:
        print("YES")