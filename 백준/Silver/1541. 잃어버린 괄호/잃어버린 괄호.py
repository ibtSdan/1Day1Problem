A = list(map(str,input().split('-')))

def mySum(i):
    sum = 0
    lst = list(map(int,i.split('+')))
    for n in lst:
        sum += n
    return sum
    
ans = mySum(A[0])    
for i in range(1, len(A)):
    ans -= mySum(A[i])
print(ans)