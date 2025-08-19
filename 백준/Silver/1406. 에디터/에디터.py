import sys
input = sys.stdin.readline

string = input().strip()
n = int(input())
left = list(string)
right = []
for _ in range(n):
    q = list(input().split())
    if q[0]=='L' and left:
        right.append(left.pop())
    elif q[0]=='D' and right:
        left.append(right.pop())
    elif q[0]=='B' and left:
        left.pop()
    elif q[0]=='P':
        left.append(q[1])

print(''.join(left+right[::-1]))