def solution(s, n):
    ans = ''
    for c in s:
        if c.isupper():
            char = ord(c)+n
            ans += chr(char) if char<=90 else chr(char-26)
        elif c.islower():
            char = ord(c)+n
            ans += chr(char) if char<=122 else chr(char-26)
        else:
            ans += ' '
    return ans