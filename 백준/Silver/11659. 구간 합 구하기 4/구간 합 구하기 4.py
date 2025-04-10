import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (n+1)
for i in range (1, n+1):
    S[i] = S[i-1] + A[i-1]
for i in range(m):
    a, b = map(int, input().split())
    print(S[b]-S[a-1])