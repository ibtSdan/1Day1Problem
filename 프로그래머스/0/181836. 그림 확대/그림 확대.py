def solution(picture, k):
    ans = []
    for s in picture:
        string = ''
        for c in s:
            string += c*k
        for _ in range(k):
            ans.append(string)
    return ans