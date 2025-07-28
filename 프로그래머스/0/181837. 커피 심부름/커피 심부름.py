def solution(order):
    ans = 0
    for i in order:
        if 'americano' in i or 'anything' in i:
            ans += 4500
        else:
            ans += 5000
    return ans