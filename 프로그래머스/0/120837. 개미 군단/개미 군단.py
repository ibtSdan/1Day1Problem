def solution(hp):
    count = 0
    count += hp//5
    hp %= 5
    count += hp//3
    hp %= 3
    count += hp//1
    return count