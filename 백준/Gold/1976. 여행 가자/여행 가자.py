import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
A[0] = [0] * (n+1)
for i in range(1,n+1):
    A[i].append(0)
    A[i].extend(list(map(int, input().split())))
        
parent = [0] * (n+1)
for i in range(1,n+1):
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

for i in range(1,n+1):
    for j in range(1,n+1):
        if A[i][j] == 1:
            union(i,j)
                
route = list(map(int, input().split()))
check = True
index = find(route[0])
for i in range(1, len(route)):
    if index != find(route[i]):
        check = False
        break
        
if check:
    print("YES")
else:
    print("NO")