def solution(number):
    number = str(number)
    ans = sum(int(s) for s in number)
    return ans%9