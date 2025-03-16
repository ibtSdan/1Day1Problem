n = int(input())
answer = []
flag = True
A = [0] * n
for i in range(n):
    A[i] = int(input())
num = 1
stack = []

for i in range(n):
    if A[i] >= num:
        while num <= A[i]:
            stack.append(num)
            num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        p = stack.pop()
        if p > A[i]:
            print("NO")
            flag = False
            break
        answer.append("-")

if flag:
    for i in answer:
        print(i)