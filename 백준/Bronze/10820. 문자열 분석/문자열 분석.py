import sys

for s in sys.stdin:
    s = s.rstrip('\n')
    lower = 0
    upper = 0
    num = 0
    b = 0
    for a in s:
        if a.islower():
            lower += 1
        elif a.isupper():
            upper += 1
        elif a.isdigit():
            num += 1
        else:
            b += 1
    print(lower,upper,num,b)