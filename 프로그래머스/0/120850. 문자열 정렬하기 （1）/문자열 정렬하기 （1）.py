def solution(my_string):
    lst = [int(i) for i in my_string if i.isdigit()]
    return sorted(lst)