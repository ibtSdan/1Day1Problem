n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input().strip())

ans = 64

for i in range(n-7):
    for j in range(m-7):
        startW = 0
        startB = 0
        for x in range(8):
            for y in range(8):
                if (x+y)%2==0:
                    if board[i+x][j+y] != 'W':
                        startW += 1
                    if board[i+x][j+y] != 'B':
                        startB += 1
                else:
                    if board[i+x][j+y] != 'B':
                        startW += 1
                    if board[i+x][j+y] != 'W':
                        startB += 1
        ans = min(ans, startW, startB)
print(ans)