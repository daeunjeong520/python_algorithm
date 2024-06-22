# 모음 제거
def solution(my_string):
    vowels = ['a', 'e', 'o', 'u', 'i']
    return "".join([i for i in my_string if i not in vowels])

print(solution("bus"))
print(solution("nice to meet you"))