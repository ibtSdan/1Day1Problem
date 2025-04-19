import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
def DFS(v):
    if len(str(v)) == n:
        print(v)
    else:
        for i in range(1,10,2):
            if isPrime(v*10+i):
                DFS(v*10+i)
            
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
    
    
DFS(2)
DFS(3)
DFS(5)
DFS(7)