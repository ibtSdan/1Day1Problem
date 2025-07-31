m, d = map(int, input().split())
days = ['SUN', 'MON','TUE','WED','THU','FRI','SAT']
if m==1 or m==10:
    print(days[d%7])
elif m==2 or m==3 or m==11:
    print(days[(d+3)%7])
elif m==4 or m==7:
    print(days[(d+6)%7])
elif m==5:
    print(days[(d+1)%7])
elif m==6:
    print(days[(d+4)%7])
elif m==8:
    print(days[(d+2)%7])
elif m==9 or m==12:
    print(days[(d+5)%7])