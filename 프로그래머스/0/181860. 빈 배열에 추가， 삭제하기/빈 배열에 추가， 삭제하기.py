def solution(arr, flag):
    ans = []
    for i in range(len(arr)):
        print(flag[i])
        if flag[i]:
            lst = [arr[i] for _ in range(arr[i]*2)]
            ans.extend(lst)
        else:
            ans = ans[:len(ans)-arr[i]]
    return ans