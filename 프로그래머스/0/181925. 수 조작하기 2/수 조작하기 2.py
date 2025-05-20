def solution(numLog):
    dic = {1:'w', -1:'s', 10:'d', -10:'a'}
    ans = ''
    for i in range(1,len(numLog)):
        n = numLog[i] - numLog[i-1]
        ans += dic[n]
    return ans