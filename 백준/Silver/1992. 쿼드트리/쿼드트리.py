import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(s for s in input()))
    
ans = ''
def check(x,y,n):
    global ans
    same = True
    first = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first != lst[i][j]:
                same = False
                break
        if not same:
            break
    if same:
        ans += first
    else:
        size = n//2
        ans += '('
        for dx in range(2):
            for dy in range(2):
                check(x+dx*size,y+dy*size,size)
        ans += ')'
    
check(0,0,n)
print(ans)