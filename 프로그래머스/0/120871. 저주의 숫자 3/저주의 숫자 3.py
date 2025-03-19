def solution(n):
    result = 0
    i = 0
    while result < n:
        i += 1
        if i%3 == 0 or '3' in str(i):
            continue
        result += 1
    return i