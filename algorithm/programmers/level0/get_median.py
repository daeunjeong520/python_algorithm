# 중앙값 구하기
def solution(array):
    return sorted(array)[len(array) // 2]

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))