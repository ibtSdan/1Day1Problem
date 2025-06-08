def solution(myString):
    ans = myString.split('x')
    ans.sort()
    return [s for s in ans if s]