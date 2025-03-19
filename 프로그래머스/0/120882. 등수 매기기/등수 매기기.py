def solution(score):
    m = []
    for i in range(len(score)):
        mean = (score[i][0] + score[i][1])/2
        m.append([mean,i])
    m.sort(key=lambda x: -x[0])
    result = [0] * len(m)
    
    rank = 1
    for i in range(len(m)):
        if i > 0 and m[i][0] == m[i-1][0]:
            result[m[i][1]] = result[m[i-1][1]]
        else:
            result[m[i][1]] = rank
        rank += 1
    
    return result