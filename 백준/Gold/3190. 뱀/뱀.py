from collections import deque

n = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]

apple = int(input())
for _ in range(apple):
    i, j = map(int, input().split())
    board[i][j] = 1 # apple = 1

ch = int(input())
change = []
for _ in range(ch):
    change.append(input().split())

dq = deque()
dq.append((1,1)) # 시작 위치
time = 0
direction = 0
idx = 0
while True:
    a, b = dq[-1]
    if direction==0: # 동
        b += 1
    elif direction==1: # 남
        a += 1
    elif direction==2: # 서
        b -= 1
    else: # 북
        a -= 1
    if a<1 or a>n or b<1 or b>n or (a,b) in dq: # 벽 or 몸에 부딪힘
        time += 1
        break

    dq.append((a,b)) # 전진 위치 추가

    if board[a][b]==0: # 사과가 없다면
        dq.popleft() # 꼬리 사라짐
    else: # 사과가 있으면
        board[a][b] = 0

    time += 1 # 이동 완료

    if idx < ch and int(change[idx][0])==time:
        if change[idx][1]=='D':
            direction = direction+1 if direction+1<4 else 0
        else: # 'L'
            direction = direction-1 if direction-1>=0 else 3
        idx += 1

print(time)