import sys
input = sys.stdin.readline

n = list(input().split('-'))
ne = 0

po = sum(list(map(int, n[0].split('+'))))

for i in range(1,len(n)):
    lst = list(map(int, n[i].split('+')))
    ne += sum(lst)
        
print(po - ne)