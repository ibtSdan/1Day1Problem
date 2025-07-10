n, m = map(int,input().split())
d = []
for _ in range(n):
    d.append(input().strip())
b = []
for _ in range(m):
    b.append(input().strip())
    
ans = set(d) & set(b)
print(len(ans))
for i in sorted(ans):
    print(i)