def solution(arr):
    arr_min = min(arr)
    arr.remove(arr_min)
    return arr if arr else [-1]