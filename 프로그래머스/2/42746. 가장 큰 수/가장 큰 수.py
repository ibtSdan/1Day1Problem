def solution(numbers):
    numbers = [str(s) for s in numbers]
    numbers.sort(key=lambda x: x*3,reverse=True)
    if numbers[0]=='0':
        return "0"
    return ''.join(s for s in numbers)