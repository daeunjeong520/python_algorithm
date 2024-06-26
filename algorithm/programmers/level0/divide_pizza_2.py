# 피자 나눠 먹기 (2)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(n):
    lcm = 6 * n // gcd(6, n)
    return lcm // 6

print(solution(6))
print(solution(10))
print(solution(4))