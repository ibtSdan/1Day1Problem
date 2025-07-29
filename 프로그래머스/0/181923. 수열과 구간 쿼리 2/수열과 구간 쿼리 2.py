def solution(arr, queries):
    ans = []
    for s,e,k in queries:
        n = 1000000
        for i in range(s,e+1):
            if arr[i]>k:
                n = min(n, arr[i])
        ans.append(n if n!=1000000 else -1)
    return ans