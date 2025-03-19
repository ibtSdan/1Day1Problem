import math
def solution(n, r):
    return math.factorial(n) // (math.factorial(r)*math.factorial(n-r))