n = int(input())
lst = list(map(int, input().split()))
m = max(lst)
print(sum(lst)*100/m/n)