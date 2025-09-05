e,s,m = map(int, input().split())
i = 1
if e==15:
    e = 0
if s==28:
    s = 0
if m==19:
    m = 0
while True:
    if i%15==e and i%28==s and i%19==m:
        print(i)
        break
    i += 1