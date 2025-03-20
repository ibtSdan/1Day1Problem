def solution(board):
    if len(board) == 1:
        return 1 if board[0][0]==0 else 0
    
    n = len(board)
    c = [[1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                c[i][j] = 0
                if i==0:
                    if j==0:
                        c[i+1][j] = c[i][j+1] = c[i+1][j+1] = 0
                    elif j==n-1:
                        c[i][j-1] = c[i+1][j] = c[i+1][j-1] = 0
                    else:
                        c[i][j-1] = c[i+1][j-1] = c[i+1][j] = c[i+1][j+1] = c[i][j+1] = 0
                elif j == 0 and i != 0:
                    if i==n-1:
                        c[i-1][j] = c[i-1][j+1] = c[i][j+1] = 0
                    else:
                        c[i-1][j] = c[i-1][j+1] = c[i][j+1] = c[j+1][j+1] = c[i+1][j] = 0
                elif i==n-1 and j != 0:
                    if j==n-1:
                        c[i-1][j] = c[i-1][j-1] = c[i][j-1] = 0
                    else:
                        c[i][j-1] = c[i-1][j-1] = c[i-1][j] = c[i-1][j+1] = c[i][j+1] = 0
                elif j==n-1 and i != 0 and i != n-1:
                    c[i-1][j] = c[i-1][j-1] = c[i][j-1] = c[i+1][j-1] = c[i+1][j] = 0
                else:
                    c[i-1][j-1]=c[i-1][j]=c[i-1][j+1]=c[i][j-1]=c[i][j+1]=c[i+1][j-1]=c[i+1][j]=c[i+1][j+1]=0
                    
    cnt = 0          
    for i in c:
        cnt += sum(1 for ii in i if ii==1)
    return cnt