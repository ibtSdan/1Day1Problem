def solution(numbers):
    result = []
    e = len(numbers)-1
    while e != 0:
        s = 0
        for _ in range(e):
            result.append(numbers[s]+numbers[e])
            s += 1
        e -= 1
    result = sorted(set(result))
    return result