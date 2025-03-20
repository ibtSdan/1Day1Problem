import heapq
def solution(n, stages):
    A = [0] * (n+1)
    for i in stages:
        if i > n:
            i = n
        for j in range(1,i+1):
            A[j] += 1
    print(A)
    fail = []
    for i in range(1,n+1):
        if A[i] == 0:
            heapq.heappush(fail, [0, i])
            continue
            
        heapq.heappush(fail, [-stages.count(i)/A[i], i])
        
    result = []
    for i in range(n):
        _, now = heapq.heappop(fail)
        result.append(now)
    return result