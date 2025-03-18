def solution(cipher, code):
    cipher = '0' + cipher
    ans = ''
    for i in range(code, len(cipher), code):
        ans += cipher[i]
    return ans