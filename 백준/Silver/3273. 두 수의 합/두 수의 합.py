import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
k = int(input())
lst.sort()

s = 0
e = n-1
cnt = 0

while s<e:
    if lst[s]+lst[e]==k:
        cnt +=1
        s += 1
        e -= 1
    elif lst[s]+lst[e] > k:
        e -= 1
    else:
        s += 1
        
print(cnt)    