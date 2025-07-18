def solution(name, yearning, photo):
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    result = []
    
    for group in photo:
        ans = 0
        for p in group:
            if p in dic:
                ans += dic[p]
        result.append(ans)
    return result