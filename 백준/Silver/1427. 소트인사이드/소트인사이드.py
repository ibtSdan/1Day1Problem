n = list(input())

for i in range(len(n)-1):
    lst = n[i:]
    m = lst.index(max(lst))
    n[m+i],n[i] = n[i],n[m+i]

for i in n:
    print(i,end='')