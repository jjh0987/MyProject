def solution(r1, r2):
    import math
    c1 = [math.sqrt(r1**2-y**2) for y in range(1,r1+1)]
    c2 = [math.sqrt(r2**2-y**2) for y in range(1,r2+1)]
    tp = [0 for _ in range(len(c2)-len(c1))]
    c1.extend(tp)
    c1 = [math.ceil(i) for i in c1]
    c2 = [math.floor(i) for i in c2]
    return sum([c2[i]-c1[i]+1 for i in range(len(c1))])*4