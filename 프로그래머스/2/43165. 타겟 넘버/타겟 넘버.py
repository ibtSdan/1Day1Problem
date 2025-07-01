import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    ans = 0
    
    def DFS(idx, currentSum):
        nonlocal ans
        
        if idx == len(numbers):
            if currentSum == target:
                ans += 1
            return
    
        DFS(idx+1, currentSum+numbers[idx])
        DFS(idx+1, currentSum-numbers[idx])
    
    DFS(0,0)
    return ans
    