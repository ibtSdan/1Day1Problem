def solution(my_string):
    lst = ['a','e','i','o','u']
    for s in lst:
        my_string = my_string.replace(s,'')
    return my_string