def solution(board, moves):
    stack = []
    ans = 0
    n = len(board)
    for i in moves:
        for j in range(n):
            if board[j][i-1]:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
        while len(stack)>=2 and stack[-1]==stack[-2]:
            ans += 1
            stack.pop()
            stack.pop()
    return ans*2