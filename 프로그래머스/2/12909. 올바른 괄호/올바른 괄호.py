def solution(s):
    lst = []
    for i in s:
        while len(lst)>1 and lst[-1]==')' and lst[-2]=='(':
            lst.pop()
            lst.pop()
        lst.append(i)
    print(lst)
    return True if lst==['(', ')'] else False