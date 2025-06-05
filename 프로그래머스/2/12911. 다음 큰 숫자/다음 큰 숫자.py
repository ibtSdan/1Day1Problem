def solution(n):
    ans = n+1
    while True:
        if bin(n)[2:].count('1') == bin(ans)[2:].count('1'):
            return ans
        else:
            ans += 1