import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    address, pw = input().split()
    dic[address] = pw
    
for _ in range(m):
    find = input().strip()
    print(dic[find])