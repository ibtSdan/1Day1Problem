def solution(arr, queries):
    for querie in queries:
        i = querie[0]
        j = querie[1]
        arr[i], arr[j] = arr[j], arr[i]
    return arr