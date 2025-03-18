def solution(age):
    A = [0] * 10
    for i in range(10):
        A[i] = chr(97+i)
    
    lst = list(map(int, str(age)))
    ans = ''
    for i in lst:
        ans += A[i]
    return ans