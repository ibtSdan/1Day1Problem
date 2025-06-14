def solution(a, d, included):
    ans = []
    for i in range(len(included)):
        ans.append(a+d*i)
    
    return sum(ans[i] for i in range(len(ans)) if included[i])