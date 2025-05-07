import sys
input = sys.stdin.readline

n = int(input())
A = {}
for _ in range(n):
    root, left, right = map(str, input().split())
    A[root] = [left, right]

def preOrder(now):
    if now == '.':
        return
    print(now, end='')
    preOrder(A[now][0])
    preOrder(A[now][1])

def inOrder(now):
    if now == '.':
        return
    inOrder(A[now][0])
    print(now, end='')
    inOrder(A[now][1])

def postOrder(now):
    if now == '.':
        return
    postOrder(A[now][0])
    postOrder(A[now][1])
    print(now, end='')
            
preOrder('A')
print()
inOrder('A')
print()
postOrder('A')