def solution(arr, i):
    ans = arr[i:]
    if 1 not in ans:
        return -1
    idx = ans.index(1)

    return idx+i if idx >= 0 else -1