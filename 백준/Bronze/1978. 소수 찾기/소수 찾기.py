n = int(input())
lst = list(map(int, input().split()))
c = 0
for i in lst:
    cc = 0
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            cc += 1
    if cc == 0:
        c += 1

if 1 in lst:
  c -= 1
print(c)