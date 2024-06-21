# 분수의 덧셈

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    g = gcd(numer, denom)

    return [numer//g, denom//g]



print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))