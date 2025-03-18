def solution(array, n):
    array.append(n)
    array = sorted(array)
    index = array.index(n)
    if index == len(array)-1:
        return array[-2]
    elif index == 0:
        return array[1]
    else:
        a = n - array[index-1]
        b = array[index+1] - n
        return array[index-1] if a<=b else array[index+1]