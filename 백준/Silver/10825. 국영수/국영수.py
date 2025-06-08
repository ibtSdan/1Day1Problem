import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    name, kor, eng, math = input().split()
    lst.append((name, int(kor), int(eng), int(math)))

lst.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for name in lst:
    print(name[0])