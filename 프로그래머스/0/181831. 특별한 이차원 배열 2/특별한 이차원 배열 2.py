def solution(arr):
    check = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                check = False
                break
    return 1 if check else 0