n = int(input())
s_index = 1
e_index = 1
count = 1
sum = 1

while e_index != n:
    if sum==n:
        count += 1
        sum -= s_index
        s_index += 1
    elif sum>n:
        sum -= s_index
        s_index += 1
    else:
        e_index += 1
        sum += e_index
    
print(count)