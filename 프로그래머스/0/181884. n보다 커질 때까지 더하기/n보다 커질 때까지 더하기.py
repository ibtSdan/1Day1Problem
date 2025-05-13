def solution(numbers, n):
    ans = 0
    i = 0
    while ans <= n:
        ans += numbers[i]
        i += 1
    return ans