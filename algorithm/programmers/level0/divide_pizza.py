# 피자 나눠 먹기 (1)
def solution(n):
    return n // 7 if n % 7 == 0 else n // 7 + 1


print(solution(7))
print(solution(1))
print(solution(15))