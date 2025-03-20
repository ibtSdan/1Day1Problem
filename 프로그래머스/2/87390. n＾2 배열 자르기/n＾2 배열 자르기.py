def solution(n, left, right):
    lst = []
    for i in range(left, right+1):
        lst.append(max(i//n, i%n)+1)
    return lst