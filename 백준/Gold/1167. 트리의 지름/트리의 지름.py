import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
A = [[] for _ in range(v+1)]
for i in range(v):
    lst = list(map(int, input().split()))
    node = lst[0]
    index = 1
    while lst[index] != -1:
        A[node].append((lst[index],lst[index+1]))
        index += 2

def BFS(s):
    dq = deque()
    visited = [-1] * (v+1)
    visited[s] = 0
    dq.append(s)
    max_node = s
    max_dis = 0
    while dq:
        node = dq.popleft()
        for a, w in A[node]:
            if visited[a] == -1:
                dq.append(a)
                visited[a] = visited[node] + w
                if visited[a] > max_dis:
                    max_node = a
                    max_dis = visited[a]
    return max_node, max_dis

start, _ = BFS(1)
_, answer = BFS(start)
print(answer)