def solution(answers):
    l = len(answers)
    n1 = [1,2,3,4,5]
    n1 = n1*(l//5)+n1[:l%5]
    n2 = [2,1,2,3,2,4,2,5]
    n2 = n2*(l//8)+n2[:l%8]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    n3 = n3*(l//10)+n3[:l%10]
    for i in range(l):
        if answers[i]==n1[i]:
            n1[i] = 0
        if answers[i]==n2[i]:
            n2[i] = 0
        if answers[i]==n3[i]:
            n3[i] = 0
    n_max = max(n1.count(0), n2.count(0), n3.count(0))
    ans = []
    if n_max<=n1.count(0):
        ans.append(1)
        n_max = n1.count(0)
    if n_max<=n2.count(0):
        ans.append(2)
        n_max = n2.count(0)
    if n_max<=n3.count(0):
        ans.append(3)
        n_max = n3.count(0)
    return sorted(ans)