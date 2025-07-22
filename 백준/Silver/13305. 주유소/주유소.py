n = int(input())
dis = list(map(int, input().split()))
exp = list(map(int, input().split()))
total = 0
min_cost = exp[0]

for i in range(n-1):
    if exp[i]<min_cost:
        min_cost = exp[i]
    total += min_cost*dis[i]
print(total)