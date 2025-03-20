def solution(babbling):
    result = 0
    s = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in s:
            i = i.replace(j, ' ')
        if i.strip() == '':
            result += 1
            
    return result