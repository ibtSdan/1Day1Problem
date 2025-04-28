import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, party_n = map(int, input().split())
true = list(map(int,input().split()))
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

check = []

for _ in range(party_n):
    party = list(map(int, input().split()))
    check.append(party[1])
    index = 0 if party[0] == 1 else party[0]+1
    first = party[1]
    for i in range(2,index):
        union(first, party[i])

cnt = 0
true_find = []
for i in range(1,len(true)):
    true_find.append(find(true[i]))

        
for i in check:
    if find(i) not in true_find:
        cnt += 1

print(cnt)