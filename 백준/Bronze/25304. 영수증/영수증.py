price = int(input())
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    price -= a*b
print("Yes" if price==0 else "No")