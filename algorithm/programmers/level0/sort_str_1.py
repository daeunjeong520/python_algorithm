# 문자열 정렬하기 (1)
def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])


print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))