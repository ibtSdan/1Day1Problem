def solution(order):
    ans = 0
    stack = []
    idx = 1
    for main in order:
        while idx<=main:
            stack.append(idx)
            idx += 1
        if stack[-1] == main:
            stack.pop()
            ans += 1
        else:
            break
    return ans