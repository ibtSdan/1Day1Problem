def solution(price):
    if price>=500000:
        percent = 0.20
    elif price>=300000:
        percent = 0.10
    elif price>=100000:
        percent = 0.05
    else:
        percent = 0
    return int(price*(1-percent))