n = int(input())
days = [0]
pays = [0]
for _ in range(n):
    day, pay = map(int, input().split())
    days.append(day)
    pays.append(pay)
D = [0]*(n+2)

for i in range(n,0,-1):
    if i+days[i]<=n+1:
        D[i] = max(D[i+1], pays[i] + D[i+days[i]])
    else:
        D[i] = D[i+1]
print(D[1])