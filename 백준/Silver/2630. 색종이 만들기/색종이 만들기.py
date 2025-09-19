n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
count = {0:0, 1:0}

def DFS(x,y,size):
    first = lst[x][y]
    same = True
    for i in range(x,x+size):
        for j in range(y,y+size):
            if lst[i][j] != first:
                same = False
                break
        if not same:
            break
    if same:
        count[first] += 1
    else:
        size //= 2
        for dx in range(2):
            for dy in range(2):
                DFS(x+dx*size,y+dy*size,size)

DFS(0,0,n)
print(count[0])
print(count[1])