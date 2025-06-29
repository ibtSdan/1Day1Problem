import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x, y = map(int,input().split())
    lst.append((x,y))
    
lst.sort(key=lambda k: (k[0],k[1]))
for x,y in lst:
    print(x, y)