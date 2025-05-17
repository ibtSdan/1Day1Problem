def solution(arr, intervals):
    ans = []
    for a, b in intervals:
        ans.extend(arr[a:b+1])
    return ans