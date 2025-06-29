import sys
input = sys.stdin.readline

n = int(input())
lst = [[] for _ in range(51)]
for _ in range(n):
    number = input().strip()
    ssum = sum(int(i) for i in number if i.isdigit())
    lst[len(number)].append((number,ssum))

for i in range(51):
    if lst[i]:
        lst[i].sort(key=lambda x: (x[1],x[0]))
        for j in lst[i]:
            print(j[0])