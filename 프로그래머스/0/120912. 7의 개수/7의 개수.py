def solution(array):
    result = 0
    for i in array:
        i = list(str(i))
        result += i.count('7')
    return result