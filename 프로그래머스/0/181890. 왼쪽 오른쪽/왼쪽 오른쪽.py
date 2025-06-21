def solution(str_list):
    l_index = str_list.index('l') if 'l' in str_list else 21
    r_index = str_list.index('r') if 'r' in str_list else 21
    if l_index<r_index:
        return str_list[:l_index]
    elif l_index>r_index:
        return str_list[r_index+1:]
    else:
        return []