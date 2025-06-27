import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    string = input().strip()
    check = True
    stack = []
    for s in string:
        if stack and s == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
        else:
            stack.append(s)
    if stack or not check:
        print("NO")
    else:
        print("YES")