def solution(intStrs, k, s, l):
    ans = []
    for string in intStrs:
        if int(string[s:s+l]) > k:
            ans.append(int(string[s:s+l]))
    return ans