import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    check = True
    word = input()
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            check = False
            break
    if check:
        cnt += 1
print(cnt)