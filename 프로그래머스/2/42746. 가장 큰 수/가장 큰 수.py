def solution(numbers):
    lst = [str(i) for i in numbers]
    lst.sort(key=lambda x: x*3, reverse=True)
    ans = ''.join(lst)
    
    return str(int(ans))