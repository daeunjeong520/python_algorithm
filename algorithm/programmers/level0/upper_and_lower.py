# 대문자와 소문자
def solution(my_string):
    answer = ""
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()

    return answer

def other_sol(my_string):
    return "".join([i.upper() if i.islower() else i.lower() for i in my_string])

print(solution("cccCCC"))
print(solution("abCdEfghIJ"))
print(other_sol("cccCCC"))
print(other_sol("abCdEfghIJ"))
