def solution(num_list, n):
    result = [[] for _ in range(len(num_list)//n)]
    index = 0
    for i in range(len(result)):
        lst = num_list[index:n+index]
        result[i] = lst
        index += n
    return result
    