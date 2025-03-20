def solution(lines):
    A = []
    for a,b in [[lines[0],lines[1]],[lines[0],lines[2]],[lines[1],lines[2]]]:
        s = max(a[0], b[0])
        e = min(a[1], b[1])
        A.extend(i for i in range(s, e))
    
    A = set(A)
    return len(A)