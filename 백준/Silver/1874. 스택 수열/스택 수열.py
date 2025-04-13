import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

a = []
ans = []
num = 1
for i in range(n):
    while num <= lst[i]:
        a.append(num)
        num += 1
        ans.append('+')
    if a[-1] == lst[i]:
        a.pop()
        ans.append('-')
    else:
        print("NO")
        sys.exit()
for i in ans:
    print(i)