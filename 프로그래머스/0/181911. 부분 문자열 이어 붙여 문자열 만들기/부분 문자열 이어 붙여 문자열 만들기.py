def solution(my_strings, parts):
    ans = ''
    for i in range(len(parts)):
        ans += my_strings[i][parts[i][0]:parts[i][1]+1]
        
    return ans