n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))
    
d = [[0 for j in range(3)] for i in range(n+1)]
d[1][1] = lst[1]

for i in range(2,n+1):
    d[i][1] = max(d[i-2][1], d[i-2][2]) + lst[i]
    d[i][2] = d[i-1][1] + lst[i]

print(max(d[n][1], d[n][2]))