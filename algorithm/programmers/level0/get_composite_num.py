# 합성수 찾기
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n):
    l = []
    for i in range(1, n+1):
        if not is_prime_num(i):
            l.append(i)
    return len(l)

def other_sol(n):
    cnt = 0
    for i in range(4, n+1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt += 1
                break
    return cnt

print(solution(10))
print(solution(15))
print(other_sol(10))
print(other_sol(15))