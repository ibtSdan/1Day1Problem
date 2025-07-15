import heapq

def solution(k, score):
    hq = []
    ans = []
    idx = k
    if k>len(score):
        k = len(score)
        
    for i in range(k):
        heapq.heappush(hq, score[i])
        ans.append(hq[0])
    while idx<len(score):
        if hq and score[idx]>=hq[0]:
            heapq.heappush(hq, score[idx])
            heapq.heappop(hq)
        elif not hq:
            heapq.heappush(hq, score[idx])
        ans.append(hq[0])
        idx += 1
    return ans