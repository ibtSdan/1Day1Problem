def solution(arr, k):
    ans = []
    for i in arr:
        if i not in ans:
            ans.append(i)
    if len(ans)==k:
        return ans
    elif len(ans)>k:
        return ans[:k]
    else:
        return ans + [-1]*(k-len(ans))