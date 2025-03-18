def solution(n):
    a = [0] * (n+1)
    result = []
    for i in range(2,n+1):
        a[i] = i
    
    for i in range(2,int(n**0.5)+1):
        if a[i] == 0:
            continue
        for j in range(i*2,n+1,i):
            a[j] = 0
    
    for i in range(2,n+1):
        if a[i]:
            result.append(i)
    
    lst = set()
    if n in result:
        return [n]
    else:
        for i in result:
            while n%i==0:
                lst.add(i)
                n = n//i
            if n==1:
                break
        lst = list(lst)
        return sorted(lst)