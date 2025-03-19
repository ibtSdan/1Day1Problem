def solution(n, words):
    a = [words[0]]
    cnt = 1
    for i in range(1,len(words)):
        a.append(words[i])
        print(a)
        if i%n==0:
            cnt += 1
        if words[i] in a[:-1] or a[i-1][-1] != words[i][0]:
            return [(i%n)+1 ,cnt]
        
    return [0,0]