n, m = map(int, input().split())
if m==1 or n==1:
    print(1)
elif n==2:
    if m==2:
        print(1)
    elif m<=4:
        print(2)
    elif m<=6:
        print(3)
    else:
        print(4)
elif m<=4:
    print(m)
elif m==5:
    print(4)
else:
    print(m-2)