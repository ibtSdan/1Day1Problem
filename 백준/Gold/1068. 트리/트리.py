import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
    
n = int(input())
A = [[] for _ in range(n)]
parent = list(map(int, input().split()))
delete_node = int(input())

def DFS(dele):
    parent[dele] = -2
    for i in range(n):
        if dele == parent[i]:
            DFS(i)

DFS(delete_node)
cnt = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:
        cnt += 1
            
print(cnt)