# 짝수의 합
def solution(n):
    return sum([i for i in range(1, n+1) if i % 2 == 0])


print(solution(10))
print(solution(4))