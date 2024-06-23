# 순서쌍 영어로
def solution(n):
    l = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            l.append(i)
            if i < n // i:
                l.append(n // i)

    return len(l)

print(solution(20))
print(solution(100))