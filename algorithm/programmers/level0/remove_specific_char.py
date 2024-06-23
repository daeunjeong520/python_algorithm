# 특정 문자 제거하기
def solution(my_string, letter):
    return "".join([i for i in my_string if i != letter])

def other_sol(my_string, letter):
    return my_string.replace(letter, '')

print(solution("abcdef", "f"))
print(solution("BCBdbe", "B"))
print(other_sol("abcdef", "f"))
print(other_sol("BCBdbe", "B"))