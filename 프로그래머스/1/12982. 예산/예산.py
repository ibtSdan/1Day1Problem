def solution(d, budget):
    result = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            return result
        result += 1
    return result