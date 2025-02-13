def solution(my_string, n):
    lst = []
    for s in my_string:
        lst.append(s*n)
    return ''.join(lst)