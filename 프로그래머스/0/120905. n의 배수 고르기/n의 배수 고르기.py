def solution(n, numlist):
    for i in range(len(numlist)):
        if numlist[i]%n!=0:
            numlist[i] = 0
    return [x for x in numlist if x!=0]