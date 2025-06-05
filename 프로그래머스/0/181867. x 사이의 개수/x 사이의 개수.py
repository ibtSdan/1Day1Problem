def solution(myString):
    ans = list(myString.split('x'))
    return [len(s) for s in ans]