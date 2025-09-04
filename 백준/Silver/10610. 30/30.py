lst = [s for s in input()]
lst.sort(reverse=True)

n = int(''.join(lst))
if n%10==0 and n%3==0:
    print(n)
else:
    print(-1)