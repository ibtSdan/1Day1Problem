def solution(sides):
    ans = sum(sides)
    result = 0
    for i in range(max(sides)+1, ans):
        result += 1
    return result*2+1