def solution(w,h):
    if w > h:
        W = h
        H = w
    else:
        W = w
        H = h

    import math
    mul = math.gcd(W,H)
    width = W//mul
    height = H//mul

    cnt = 0
    loc = [height * (i / width) for i in range(width + 1)]
    for i in range(len(loc) - 1):
        cnt += len(range(math.floor(loc[i]), math.ceil(loc[i + 1])))
    return w*h - cnt*mul