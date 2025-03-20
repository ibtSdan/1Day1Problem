n = int(input())
m = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0
s = 0
e = n-1
while s < e:
    if A[s]+A[e] == m:
        cnt += 1
        s += 1
        e -= 1
    elif A[s]+A[e] > m:
        e -= 1
    else:
        s += 1
print(cnt)