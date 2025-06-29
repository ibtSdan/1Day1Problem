def solution(array, commands):
    ans = []
    for i,j,k in commands:
        a = array[i-1:j]
        a.sort()
        ans.append(a[k-1])
    return ans