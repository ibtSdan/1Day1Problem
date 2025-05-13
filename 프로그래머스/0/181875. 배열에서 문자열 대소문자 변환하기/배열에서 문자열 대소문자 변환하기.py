def solution(strArr):
    return [strArr[s].lower() if s%2==0 else strArr[s].upper() for s in range(len(strArr))]