def solution(s):
    stack = []
    is_valid = True
    for i in s:
        if i==')':
            if not stack or stack[-1] != '(':
                is_valid = False
                break
            else:
                stack.pop()
        else:
            stack.append(i)
    if stack:
        is_valid = False
        
    return is_valid