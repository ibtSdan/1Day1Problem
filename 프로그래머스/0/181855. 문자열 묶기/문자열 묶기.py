def solution(strArr):
    dic = {}
    for s in strArr:
        l = len(s)
        if l not in dic:
            dic[l] = 1
        else:
            dic[l] += 1

    ans = 0
    for key in dic:
        if dic[key]>ans:
            ans = dic[key]
    return ans