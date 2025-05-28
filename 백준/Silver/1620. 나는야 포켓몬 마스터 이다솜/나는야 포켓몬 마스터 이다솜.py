import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_to_name = {}
name_to_num = {}
for i in range(1,n+1):
    s = input().strip()
    num_to_name[i] = s
    name_to_num[s] = i

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(num_to_name[int(q)])
    else:
        print(name_to_num[q])