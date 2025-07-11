from collections import deque

def solution(progresses, speeds):
    ans = []
    dq = deque()
    for i in range(len(progresses)):
        dq.append([progresses[i], speeds[i]])
    while dq:
        while dq[0][0]<100:
            for i in range(len(dq)):
                dq[i][0] += dq[i][1]
        cnt = 0
        while dq and dq[0][0]>=100:
            cnt += 1
            dq.popleft()
        ans.append(cnt)
    return ans