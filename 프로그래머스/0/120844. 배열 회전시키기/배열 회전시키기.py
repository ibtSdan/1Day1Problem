def solution(numbers, direction):
    result = []
    if direction == 'right':
        result.append(numbers[-1])
        for i in range(len(numbers)-1):
            result.append(numbers[i])
    else:
        for i in range(len(numbers)-1):
            result.append(numbers[i+1])
        result.append(numbers[0])
    return result