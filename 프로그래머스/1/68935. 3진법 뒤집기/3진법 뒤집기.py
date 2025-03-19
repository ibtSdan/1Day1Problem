import numpy

def solution(n):
    n = numpy.base_repr(n, base=3)
    n = str(n)[::-1]
    return int(n,3)