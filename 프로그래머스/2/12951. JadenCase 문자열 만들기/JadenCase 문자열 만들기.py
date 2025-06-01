def solution(s):
    s = s.lower()
    result = ''
    check = True
    for i in s:
        if i==' ':
            result += i
            check = True
        elif check:
            result += i.upper()
            check = False
        else:
            result += i
    return result