def solution(emergency):
    a = sorted(emergency, reverse=True)
    result = [0] * len(a)
    for i in range(len(emergency)):
        n = emergency.index(a[i])
        result[n] = i+1
    return result