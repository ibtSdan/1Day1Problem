import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
S = [0]*N
S[0] = A[0]
M_list = [0]*M

for i in range(1,N):
    S[i] = S[i-1]+A[i]

for i in S:
    remainder = i%M
    if remainder == 0:
        cnt += 1
    M_list[remainder] += 1

for i in M_list:
    if i>1:
        cnt += i*(i-1)//2

print(cnt)
    
# s[i]%m == s[j]%m 이면, i+1부터j는 m으로 나누어떨어짐