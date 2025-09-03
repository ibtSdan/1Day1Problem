import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
count = {-1:0,0:0,1:0}

def check(x,y,n):
    first = lst[x][y]
    same = True
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first != lst[i][j]:
                same = False
                break
        if not same:
            break
    if same:
        count[first] += 1
    else:
        size = n//3
        for dx in range(3):
            for dy in range(3):
                check(x+dx*size,y+dy*size,size)

    
check(0,0,n)
print(count[-1])
print(count[0])
print(count[1])