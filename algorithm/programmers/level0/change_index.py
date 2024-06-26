# 인덱스 바꾸기
def solution(my_string, num1, num2):
    l = list(my_string)
    l[num1], l[num2] = l[num2], l[num1]
    return "".join(l)

print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))