import sys

n = int(input())

def isPrime(x):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if x%i==0:
            return False
    return True
    
def isPalin(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
        
while True:
    if isPrime(n) and isPalin(n):
        print(n)
        sys.exit()
    n += 1