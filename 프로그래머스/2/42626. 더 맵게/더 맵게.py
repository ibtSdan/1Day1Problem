import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    check = True
    cnt = 0
    
    while any(i < k for i in scoville):
        if len(scoville)==1:
            check = False
            break
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, first+second*2)
            cnt += 1
            
    if check:
        return cnt
    else:
        return -1