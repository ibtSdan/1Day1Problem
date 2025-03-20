def solution(s):
    l = ['()', '{}', '[]']
    result = 0
    for i in range(len(s)):
        a = s[i:] + s[:i]
        while '()' in a or '{}' in a or '[]' in a:
            a = a.replace('()', '')
            a = a.replace('{}', '')
            a = a.replace('[]', '')
        if not a:
            result += 1
    return result