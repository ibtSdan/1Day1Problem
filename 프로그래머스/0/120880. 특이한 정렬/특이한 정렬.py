import heapq
def solution(numlist, n):
    result = []
    minus = []
    for i in numlist:
        heapq.heappush(minus, (abs(n-i),-i))
        
    for _ in range(len(numlist)):
        _, n = heapq.heappop(minus)
        result.append(-n)
    return result