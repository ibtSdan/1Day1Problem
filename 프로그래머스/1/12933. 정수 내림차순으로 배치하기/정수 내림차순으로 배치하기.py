def solution(n):
    n = sorted(str(n), reverse=True)
    ans = ''.join(i for i in n)
    return int(ans)