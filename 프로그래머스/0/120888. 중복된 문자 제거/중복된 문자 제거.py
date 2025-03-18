def solution(my_string):
    result = ''
    for s in my_string:
        if s in result:
            continue
        result += s
    return result