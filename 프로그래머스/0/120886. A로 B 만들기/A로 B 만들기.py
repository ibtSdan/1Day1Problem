def solution(before, after):
    s = set(before)
    for i in s:
        if after.count(i) != before.count(i):
            return 0
    return 1