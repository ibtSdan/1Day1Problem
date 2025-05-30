def solution(myString, pat):
    s = ''.join('A' if s=='B' else 'B' for s in myString)
    return 1 if pat in s else 0