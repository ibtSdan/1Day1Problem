import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
def check(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        return False
    return True

    
for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    else:
        if check(a,b):
            print("YES")
        else:
            print("NO")