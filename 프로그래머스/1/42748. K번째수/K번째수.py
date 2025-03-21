def solution(array, commands):
    ans = []
    for i in commands:
        lst = array[i[0]-1:i[1]]
        lst.sort()
        ans.append(lst[i[2]-1])
    return ans