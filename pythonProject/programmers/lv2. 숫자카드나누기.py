arrayA = [10,17]
arrayB = [5,20]
import math
# a = math.gcd(*arrayA)
# b = math.gcd(*arrayB)

def solution(arrayA, arrayB):
    import math
    a = arrayA[0]
    for i in range(1, len(arrayA)):
        a = math.gcd(a, arrayA[i])
    b = arrayB[0]
    for i in range(1, len(arrayB)):
        b = math.gcd(b, arrayB[i])

    if math.gcd(a, b) == 1:
        return max(a, b)
    return 0

solution(arrayB,arrayA)