s, p = map(int, input().split())
password = input()
lst = list(map(int, input().split()))
c_dic = {'A':lst[0], 'C':lst[1], 'G':lst[2], 'T':lst[3]}

psw = password[:p]
p_dic = {'A':psw.count('A'),'C':psw.count('C'),'G':psw.count('G'),'T':psw.count('T')}

cnt = 1 if all(p_dic[key]>=c_dic[key] for key in 'ACGT') else 0

for i in range(1,s-p+1):
    p_dic[password[i-1]] -= 1
    p_dic[password[i+p-1]] += 1
    
    if all(p_dic[key]>=c_dic[key] for key in 'ACGT'):
        cnt += 1

print(cnt)