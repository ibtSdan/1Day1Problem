from collections import deque

n = int(input())
A = [[] for _ in range(n+1)]
D = [0] * (n+1)
time = [0] * (n+1)
total = [0] * (n+1)

for num in range(1, n+1):
    lst = list(map(int, input().split()))
    for i in range(len(lst)-1):
        if i==0:
            time[num] = lst[i]
        else:
            A[lst[i]].append(num)
            D[num] += 1
            
dq = deque()
for i in range(1, n+1):
    if D[i]==0:
        dq.append(i)
        
while dq:
    now = dq.popleft()
    for i in A[now]:
        D[i] -= 1
        total[i] = max(total[i], total[now]+time[now])
        if D[i]==0:
            dq.append(i)
            
for i in range(1,n+1):
    print(total[i]+time[i])