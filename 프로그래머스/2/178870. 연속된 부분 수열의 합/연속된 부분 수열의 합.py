def solution(sequence, k):
    ans = []
    length = len(sequence)
    s = 0
    e = 0
    total = 0
    
    while True:
        if total >= k:
            if total==k:
                if e-s-1 < length:
                    ans = [s,e-1]
                    length = e-s-1
            total -= sequence[s]
            s += 1
        elif e == len(sequence):
            break
        else:
            total += sequence[e]
            e += 1
            
    return ans