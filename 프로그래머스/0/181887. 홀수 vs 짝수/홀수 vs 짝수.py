def solution(num_list):
    odd_sum = sum(num_list[i] for i in range(len(num_list)) if i%2==0)
    even_sum = sum(num_list[i] for i in range(len(num_list)) if i%2==1)
    return max(odd_sum, even_sum)