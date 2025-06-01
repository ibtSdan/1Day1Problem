def solution(n):
    ans = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        ans[i][i] = 1
    return ans