def solution(n):
    ans = 0
        
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            ans = ans + i + n//i
            print(ans)
            
    if int(n**0.5) == n**0.5:
        ans -= n**0.5
            
    return ans