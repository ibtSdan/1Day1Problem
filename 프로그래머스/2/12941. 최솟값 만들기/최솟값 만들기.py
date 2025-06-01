def solution(A,B):
    ans = 0
    A.sort(reverse=True)
    B.sort()
    for _ in range(len(A)):
        a_max = A.pop()
        b_min = B.pop()
        ans += a_max * b_min
        
    return ans