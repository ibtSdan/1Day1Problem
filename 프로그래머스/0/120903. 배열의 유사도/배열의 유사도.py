def solution(s1, s2):
    result = 0
    for s in s1:
        if s in s2:
            result += 1
    
    return result