def solution(num_list):
    lst = [0,0]
    for i in num_list:
        if i%2==0:
            lst[0] += 1
        else:
            lst[1] += 1
    return lst