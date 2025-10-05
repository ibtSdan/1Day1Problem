lst = [0]
n_gears = 4
for _ in range(4):
    lst.append(list(map(int,input().strip())))

def clock(lst):
    return [lst[-1]] + lst[:7]

def re(lst):
    return lst[1:] + [lst[0]]

test = int(input())
for _ in range(test):
    gear, direction = map(int, input().split())
    check = [0]*(n_gears+1)
    check[gear] = direction

    for i in range(gear,n_gears):
        if lst[i][2] != lst[i+1][6]:
            check[i+1] = -check[i]
        else:
            break
    for i in range(gear,1,-1):
        if lst[i][6] != lst[i-1][2]:
            check[i-1] = -check[i]
        else:
            break

    for i in range(1,n_gears+1):
        if check[i]==1:
            lst[i] = clock(lst[i])
        elif check[i]==-1:
            lst[i] = re(lst[i])

ans = 0
for i in range(1,n_gears+1):
    if lst[i][0]==1:
        ans += (1<<(i-1))
print(ans)