s = input().strip()
while len(s)%3!=0:
    s = '0' + s
    
ans = []
for i in range(0,len(s),3):
    n = s[i:i+3]
    ans.append(int(n[0])*4+int(n[1])*2+int(n[2])*1)
print(''.join(map(str, ans)))