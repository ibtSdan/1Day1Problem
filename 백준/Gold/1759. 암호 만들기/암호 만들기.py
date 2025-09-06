n, k = map(int, input().split())
lst = list(map(str,input().split()))
lst.sort()
ans = []
mo = ['a','e','i','o','u']

def check(s):
    ja_check = False
    mo_check = False
    cnt = 0
    for c in s:
        if c in mo:
            mo_check = True
        else:
            cnt += 1
    if cnt>=2:
        ja_check = True
    return mo_check and ja_check

def DFS(s,i):
    if len(s)==n:
        if check(s):
            ans.append(s)
    else:
        for idx in range(i+1,k):
            DFS(s+lst[idx], lst.index(lst[idx]))

for i in range(k):
    DFS(lst[i],i)

for i in ans:
    print(i)