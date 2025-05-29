def solution(myString):
    a = 'abcdefghijk'
    return ''.join('l' if s in a else s for s in myString)