import sys
input = sys.stdin.readline

string = input().strip()
n = int(input())
for _ in range(n):
    c, s, e = input().split()
    print(string[int(s):int(e)+1].count(c))