# 숫자 찾기
def solution(num, k):
    answer = str(num).find(str(k))
    return -1 if str(k) not in str(num) else answer + 1

print(solution(20183, 1))
print(solution(232443, 4))
print(solution(123456, 7))