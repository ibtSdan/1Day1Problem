def solution(numbers, k):
    index = 0
    for _ in range(k-1):
        if index==len(numbers)-1:
            index = 1
        elif index==len(numbers)-2:
            index = 0
        else:
            index += 2
    return index+1