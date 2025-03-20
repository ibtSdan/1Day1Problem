def solution(d):
    A = [[d[0],d[1],d[2],d[3]]
         ,[d[0],d[2],d[1],d[3]]
         ,[d[0],d[3],d[1],d[2]]
         ,[d[1],d[2],d[0],d[3]]
         ,[d[1],d[3],d[0],d[2]]
         ,[d[2],d[3],d[0],d[1]]]
    
    for a1,a2,b1,b2 in A:
        adx = abs(a2[0]-a1[0])
        ady = abs(a2[1]-a1[1])
        bdx = abs(b2[0]-b1[0])
        bdy = abs(b2[1]-b1[1])
        
        if ady/adx == bdy/bdx:
            return 1
        
    return 0