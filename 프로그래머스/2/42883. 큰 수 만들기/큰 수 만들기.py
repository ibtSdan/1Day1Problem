def solution(number, k):
    number = [int(i) for i in number]
    stack = []
    ans = []
    for i in range(len(number)):
        while stack and number[i] > stack[-1] and k>0:
            stack.pop()
            k -= 1
        stack.append(number[i])
        if k==0:
            ans = stack + number[i+1:]
            break
    if k:
        ans = stack[:len(stack)-k]
    return ''.join(str(s) for s in ans)