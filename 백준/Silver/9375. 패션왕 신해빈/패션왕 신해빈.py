import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    dic = {}
    for _ in range(n):
        dress, type = input().split()
        if type in dic:
            dic[type] += 1
        else:
            dic[type] = 1
            
    mul = 1
    for type in dic:
        mul = mul * (dic[type]+1)
    print(mul-1)