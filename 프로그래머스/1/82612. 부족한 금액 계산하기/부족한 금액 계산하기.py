def solution(price, money, count):
    A = [i for i in range(price,price*count+1,price)]
    S = [0] * count
    S[0] = A[0]
    for i in range(1,count):
        S[i] = S[i-1] + A[i]
    return S[-1]-money if S[-1]>money else 0