h, m = map(int, input().split())
plus = int(input())

m = m+plus%60
h = h+plus//60

if m>=60:
    m = m-60
    h = h+1
    
while h>=24:
    h = h-24
    
print(h, m)