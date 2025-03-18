def solution(my_str, n):
    result = []
    for i in range(len(my_str)//n):
        result.append(my_str[i*n:(i+1)*n])
    if len(my_str) > len(my_str)//n * n:
        result.append(my_str[len(my_str)//n*n:])
    return result