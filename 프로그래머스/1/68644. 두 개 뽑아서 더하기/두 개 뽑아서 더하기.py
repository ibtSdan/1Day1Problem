def solution(numbers):
    result = []
    s = 0
    while s < len(numbers)-1:
        for e in range(s+1,len(numbers)):
            result.append(numbers[s]+numbers[e])
        s += 1
    return sorted(list(set(result)))