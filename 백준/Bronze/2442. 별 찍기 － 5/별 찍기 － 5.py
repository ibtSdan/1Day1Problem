n = int(input())
for i in range(1,n):
    print(' '*(n-i)+'*'*(2*i-1)+' ')
print('*'*(2*n-1))