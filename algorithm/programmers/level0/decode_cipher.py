# 암호 해독
def solution(cipher, code):
    return "".join([cipher[i] for i in range(code-1, len(cipher), code)])

def other_sol(cipher, code):
    return cipher[code-1::code]


print(solution("dfjardstddetckdaccccdegk", 4))
print(solution("pfqallllabwaoclk", 2))

print(other_sol("dfjardstddetckdaccccdegk", 4))
print(other_sol("pfqallllabwaoclk", 2))