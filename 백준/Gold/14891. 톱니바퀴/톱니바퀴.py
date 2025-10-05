lst = [0]
for _ in range(4):
    lst.append(list(map(int,input().strip())))

def clock(lst):
    return [lst[-1]] + lst[:7]

def re(lst):
    return lst[1:] + [lst[0]]

test = int(input())
for _ in range(test):
    n, di = map(int,input().split())
    check = [0]*5
    check[n] = di
    if n==1:
        if lst[n][2] != lst[n+1][6]:
            check[n+1] = check[n]*-1
        if lst[n+1][2] != lst[n+2][6]:
            check[n+2] = check[n+1]*-1
        if lst[n+2][2] != lst[n+3][6]:
            check[n+3] = check[n+2]*-1
    elif n==2:
        if lst[n][6] != lst[n-1][2]:
            check[n-1] = check[n]*-1
        if lst[n][2] != lst[n+1][6]:
            check[n+1] = check[n]*-1
        if lst[n+1][2] != lst[n+2][6]:
            check[n+2] = check[n+1]*-1
    elif n==3:
        if lst[n][6] != lst[n-1][2]:
            check[n-1] = check[n]*-1
        if lst[n-1][6] != lst[n-2][2]:
            check[n-2] = check[n-1]*-1
        if lst[n][2] != lst[n+1][6]:
            check[n+1] = check[n]*-1
    else:
        if lst[n][6] != lst[n-1][2]:
            check[n-1] = check[n]*-1
        if lst[n-1][6] != lst[n-2][2]:
            check[n-2] = check[n-1]*-1
        if lst[n-2][6] != lst[n-3][2]:
            check[n-3] = check[n-2]*-1

    for i in range(1,5):
        if check[i]==1:
            lst[i] = clock(lst[i])
        elif check[i]==-1:
            lst[i] = re(lst[i])

ans = 0  
if lst[1][0]==1:
    ans += 1
if lst[2][0]==1:
    ans += 2
if lst[3][0]==1:
    ans += 4
if lst[4][0]==1:
    ans += 8
print(ans)