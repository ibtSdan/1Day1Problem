s = list(input().split('-'))
ans = 0
def ssum(a):
  lst = list(map(int, a.split('+')))
  return sum(lst)

for i in range(len(s)):
  if i==0:
    ans += ssum(s[i])
  else:
    ans -= ssum(s[i])
print(ans)