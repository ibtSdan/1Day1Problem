def solution(array):
    s = set(array)
    A = []
    for i in s:
        A.append([array.count(i),i])
    
    m = max(i[0] for i in A)

    result = list(i[1] for i in A if i[0]==m)
    
    if len(result) > 1:
        return -1
    else:
        return result[0]