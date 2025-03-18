def solution(i, j, k):
    result = 0
    for a in range(i,j+1):
        a = list(map(int,str(a)))
        result += a.count(k)
    return result