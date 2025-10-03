lst = [i for i in range(10001)]
lst[1] = 0
for i in range(2,int(10000**0.5)+1):
    if lst[i]==0:
        continue
    for j in range(i*2, 10001, i):
        lst[j] = 0

test = int(input())
for _ in range(test):
    n = int(input())
    s = e = n//2
    while s>0:
        if lst[s] and lst[e]:
            print(s, e)
            break
        s -= 1
        e += 1