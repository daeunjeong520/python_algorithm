# 숨어 있는 숫자의 덧셈 (1)
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdecimal()])

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))