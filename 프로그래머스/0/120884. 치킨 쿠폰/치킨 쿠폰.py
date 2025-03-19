def solution(chicken):
    service = 0
    c = chicken
    while c >= 10:
        new = c // 10
        service += new
        c = c%10 + new
    return service
        