def solution(A, B):
    if A == B:
        return 0
    
    result = 0
    for _ in range(len(A)-1):
        A = shift(A)
        result += 1
        if A==B:
            return result
    return -1

def shift(s):
    return s[-1] + s[:-1]