def solution(nums):
    nums.sort()
    A = make(nums[-1]+nums[-2]+nums[-3])
    result = 0
    
    print(A)
    for i in range(len(nums)-2):
        m = i+1
        while m < len(nums)-1:
            e = m+1
            while e < len(nums):
                if nums[i]+nums[m]+nums[e] in A:
                    result += 1
                e += 1
            m += 1
    return result
    
    
    
def make(n):
    A = [0] * (n+1)
    for i in range(2,n+1):
        A[i] = i
    for i in range(2,int(n**0.5)+1):
        if A[i]==0:
            continue
        for j in range(i*2,n+1,i):
            A[j] = 0
    return [i for i in A if i]