def solution(dots):
    a = max(dots[0][0],dots[1][0],dots[2][0],dots[3][0])
    b = min(dots[0][0],dots[1][0],dots[2][0],dots[3][0])
    c = max(dots[0][1],dots[1][1],dots[2][1],dots[3][1])
    d = min(dots[0][1],dots[1][1],dots[2][1],dots[3][1])
    
    return (a-b) * (c-d)