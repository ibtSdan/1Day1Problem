def solution(elements):
    lst = elements + elements[:len(elements)-1]
    ans = []
    for k in range(1,len(elements)+1):
        total = sum(lst[:k])
        ans.append(total)
        for i in range(k,k+len(elements)-1):
            total = total + lst[i] - lst[i-k]
            ans.append(total)
    return len(set(ans))