def solution(s):
    zero = 0
    cnt = 0
    while s!="1":
        cnt += 1
        zero += list(s).count('0')
        s = s.replace('0','')
        l = len(s)
        s = bin(l)[2:]
    return [cnt,zero]