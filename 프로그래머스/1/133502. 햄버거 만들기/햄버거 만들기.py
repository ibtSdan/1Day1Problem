def solution(ingredient):
    lst = []
    bread = 0
    cnt = 0
    for i in ingredient:
        lst.append(i)
        if len(lst)>=4:
            if lst[-1]==1 and lst[-2]==3 and lst[-3]==2 and lst[-4]==1:
                for _ in range(4):
                    lst.pop()
                cnt += 1
    return cnt