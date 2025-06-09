def solution(cards1, cards2, goal):
    idx = 0
    idx1 = 0
    idx2 = 0
    cnt = 0
    while idx<len(goal):
        if idx1<len(cards1) and goal[idx]==cards1[idx1]:
            idx1 += 1
            cnt += 1
        elif idx2<len(cards2) and goal[idx]==cards2[idx2]:
            idx2 += 1
            cnt += 1
        idx += 1
    
    if cnt == len(goal):
        return "Yes"
    else:
        return "No"