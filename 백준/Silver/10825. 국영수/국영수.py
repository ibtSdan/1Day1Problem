import sys
input = sys.stdin.readline


n = int(input())
A = []
for _ in range(n):
    name, kor, eng, math = input().split()
    A.append((name, int(kor), int(eng), int(math)))

A.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name in A:
    print(name[0])