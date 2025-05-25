n = int(input())
lst = list(map(int, input().split()))

no_del = [0]*n
one_del = [0]*n

no_del[0] = lst[0]
one_del[0] = float('-inf')
ans = lst[0]

for i in range(1,n):
    no_del[i] = max(no_del[i-1]+lst[i], lst[i])
    one_del[i] = max(one_del[i-1]+lst[i], no_del[i-1])
    ans = max(ans, no_del[i], one_del[i])
    
print(ans)