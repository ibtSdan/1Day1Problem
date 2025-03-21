def solution(sizes):
    maxx = []
    minn = []
    for i in sizes:
        maxx.append(max(i[0],i[1]))
        minn.append(min(i[0],i[1]))
    return max(maxx)*max(minn)