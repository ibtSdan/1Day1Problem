import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    
    while any(i < K for i in scoville):
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second*2
        heapq.heappush(scoville, new)
        ans += 1

    return ans