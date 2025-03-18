import math
a, b = map(int, input().split())
cnt = b-a+1
check = [False]*(b-a+1)

for i in range(2, int(math.sqrt(b)+1)):
    pow = i*i
    start = pow * (a//pow+1) if a%pow!=0 else a
    for j in range(start,b+1,pow):
        if not check[j-a]:
            cnt -= 1
            check[j-a] = True

print(cnt)