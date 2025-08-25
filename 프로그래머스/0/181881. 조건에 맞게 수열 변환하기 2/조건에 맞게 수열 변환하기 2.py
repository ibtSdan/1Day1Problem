def solution(arr):
    ans = 0
    while True:
        arr2 = []
        for i in arr:
            if i>=50 and i%2==0:
                i//=2
            elif i<50 and i%2==1:
                i = i*2 + 1
            arr2.append(i)
        if arr==arr2:
            return ans
            break
        arr = arr2
        ans += 1