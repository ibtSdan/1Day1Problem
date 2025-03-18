def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    lst = list(map(int, s.split()))
    return sum(lst)