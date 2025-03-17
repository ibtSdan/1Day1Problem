import sys, math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())

# DFS
def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1,10,2):
            if isPrime(number*10+i):
                DFS(number*10+i)

# 소수 판별
def isPrime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            return False
    return True


DFS(2)
DFS(3)
DFS(5)
DFS(7)