def solution(box, n):
    d = 1
    for i in range(2):
        d *= box[i]//n
    
    return d * (box[2]//n)