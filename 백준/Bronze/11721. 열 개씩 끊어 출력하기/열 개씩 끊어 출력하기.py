s = input()
for i in range(len(s)//10):
    print(s[i*10:(i+1)*10])
if len(s)%10 != 0:
    print(s[-(len(s)%10):])