n = int(input())
lst = list(map(int, input().split()))
lst_max = max(lst)
m = 0
for i in lst:
    m += (i/lst_max)*100
print(m/n)