import sys
input = sys.stdin.readline

lst = [i for i in range(1000001)]
lst[1] = 0
for i in range(2,int(1000001**0.5)+1):
    if lst[i]==0:
        continue
    for j in range(i*2,1000001,i):
        lst[j] = 0

while True:
    check = False
    n = int(input())
    if n==0:
        break
    for s in range(3,n,2):
        if lst[s] and lst[n-s]:
            check = True
            print(f'{n} = {s} + {n-s}')
            break
    
    if not check:
        print("Goldbach's conjecture is wrong.")