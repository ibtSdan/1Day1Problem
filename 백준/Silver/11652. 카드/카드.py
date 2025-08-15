n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
dic = {}
for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

ans = []
num = max(dic.values())
for i in dic:
    if dic[i]>=num:
        ans.append(i)
print(min(ans))