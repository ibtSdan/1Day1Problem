def solution(my_string, is_prefix):
    n = len(is_prefix)
    return 1 if my_string[:n]==is_prefix else 0