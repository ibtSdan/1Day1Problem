def solution(my_string):
    result = ''
    for s in my_string:
        result += s.upper() if s.islower() else s.lower()
    return result