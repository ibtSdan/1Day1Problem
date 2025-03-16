import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
cnt = 0

for k in range(n):
    s = 0
    e = n-1
    while s<e:
        if A[s]+A[e] == A[k]:
            if s != k and e != k:
                cnt += 1
                break
            if s == k:
                s += 1
            else:
                e -= 1
        elif A[s]+A[e] > A[k]:
            e -= 1
        else:
            s += 1
print(cnt)