import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n = int(input())
    lst = list(map(int, input().split()))
    A = [[] for _ in range(n+1)]
    for i in range(n):
        A[i+1].append(lst[i])
        
    def DFS(v):
        visited[v] = True
        for i in A[v]:
            if not visited[i]:
                DFS(i)
    
    visited = [False] * (n+1)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            DFS(i)
            cnt += 1
    print(cnt)