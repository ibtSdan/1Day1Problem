import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()
m = int(input())
find = list(map(int,input().split()))

for i in range(m):
    flag = False
    target = find[i]
    s = 0
    e = len(A) - 1
    while s <= e:
        mid = (s+e)//2
        if A[mid] > target:
            e = mid - 1
        elif A[mid] < target:
            s = mid + 1
        else:
            flag = True
            break
    if flag:
        print(1)
    else:
        print(0)