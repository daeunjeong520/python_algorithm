# 피자 나눠 먹기(3)
def solution(slice, n):
    return n // slice if n % slice == 0 else n // slice + 1


print(solution(7, 10))
print(solution(4, 12))