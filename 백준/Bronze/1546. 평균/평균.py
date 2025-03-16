n = int(input())
lst = list(map(int, input().split()))
mymax = max(lst)
print(sum(lst)/mymax*100/len(lst))