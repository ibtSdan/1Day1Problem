import sys
input = sys.stdin.readline
swap = 0

# 병합 정렬
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    
    return merge(left, right)

# 병합
def merge(left, right):
    global swap
    i = j = 0
    sorted_A = []
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sorted_A.append(left[i])
            i += 1
        else:
            swap += len(left) - i
            sorted_A.append(right[j])
            j += 1
    sorted_A.extend(left[i:])
    sorted_A.extend(right[j:])
    
    return sorted_A

    
# 입력
n = int(input())
A = list(map(int, input().split()))
merge_sort(A)
print(swap)