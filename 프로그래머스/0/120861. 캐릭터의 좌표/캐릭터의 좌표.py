def solution(keyinput, board):
    a = [0,0]
    for i in keyinput:
        if i == 'left':
            a[0] += -1
            if a[0] < -(board[0]//2):
                a[0] += 1
        elif i == 'right':
            a[0] += 1
            if a[0] > board[0]//2:
                a[0] += -1
        elif i == 'up':
            a[1] += 1
            if a[1] > board[1]//2:
                a[1] += -1
        else:
            a[1] += -1
            if a[1] < -(board[1]//2):
                a[1] += 1
    return a