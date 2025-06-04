def solution(arr):
    ans = []
    for i in arr:
        lst = [i] * i
        ans.extend(lst)
    return ans