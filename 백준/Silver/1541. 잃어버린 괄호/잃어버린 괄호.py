A = list(input().split('-'))
ans = 0

for i in range(len(A)):
    B = list(map(int, A[i].split('+')))
    if i==0:
        ans += sum(B)
    else:
        ans -= sum(B)
print(ans)