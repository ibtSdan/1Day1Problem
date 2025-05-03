def solution(num_list):
    mul = 1
    summ = 0
    for i in num_list:
        mul *= i
        summ += i
        
    return 1 if mul < summ**2 else 0