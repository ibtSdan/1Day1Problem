def solution(x):
    x_sum = sum(int(i) for i in str(x))
    return True if x%x_sum==0 else False