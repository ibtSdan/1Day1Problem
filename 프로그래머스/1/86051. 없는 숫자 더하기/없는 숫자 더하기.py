def solution(numbers):
    lst = [i for i in range(10)]
    for i in numbers:
        lst.remove(i)
    return sum(lst)