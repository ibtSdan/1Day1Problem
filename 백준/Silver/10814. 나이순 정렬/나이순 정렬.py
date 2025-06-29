import sys
input = sys.stdin.readline

n = int(input())
lst = [[] for _ in range(201)]

for _ in range(n):
    age, name = input().split()
    lst[int(age)].append(name)

for i in range(1,201):
    if lst[i]:
        for name in lst[i]:
            print(str(i)+" "+name)