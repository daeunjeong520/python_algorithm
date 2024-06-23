# 문자열 정렬하기 (2)
def solution(my_string):
    return "".join(sorted(my_string.lower()))


print(solution("Bcad"))
print(solution("heLLo"))
print(solution("Python"))