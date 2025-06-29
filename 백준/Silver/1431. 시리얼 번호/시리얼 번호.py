import sys
input = sys.stdin.readline

n = int(input())
lst = [input().strip() for _ in range(n)]

def sort_key(s):
    ssum = sum(int(i) for i in s if i.isdigit())
    return (len(s), ssum, s)

lst.sort(key=sort_key)
for se in lst:
    print(se)