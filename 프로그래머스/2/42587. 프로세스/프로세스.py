from collections import deque

def solution(priorities, location):
    lst = [i for i in range(len(priorities))]
    dq = deque(lst)
    cnt = 0
    check = True
    while check:
        n = dq.popleft()
        if priorities[n] < max(priorities):
            dq.append(n)
        else:
            cnt += 1
            priorities[n] = 0
            if n==location:
                check = False
    return cnt