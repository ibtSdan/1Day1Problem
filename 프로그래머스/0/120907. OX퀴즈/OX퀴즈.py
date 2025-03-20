def solution(quiz):
    result = []
    for i in quiz:
        i = i.replace(' ', '')
        a, b = i.split('=')
        if eval(a) == int(b):
            result.append("O")
        else:
            result.append("X")
    return result