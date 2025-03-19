def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        n1 = make_n(bin(arr1[i])[2:],n)
        n2 = make_n(bin(arr2[i])[2:],n)
        k = ''
        for j in range(n):
            if n1[j]=='1' or n2[j]=='1':
                k += '#'
            else:
                k += ' '
        result.append(k)
        
    return result

        
def make_n(s,n):
    if len(s)<n:
        return "0"*(n-len(s))+s
    return s