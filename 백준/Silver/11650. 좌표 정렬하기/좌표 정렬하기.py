n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append([x,y])
    
lst.sort()
for x,y in lst:
    print(x, y)