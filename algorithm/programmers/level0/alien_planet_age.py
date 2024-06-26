# 외계 행성 나이
def solution(age):
    start_char = 'a'
    l = [chr(i) for i in range(ord(start_char), ord(start_char) + 26)]
    answer = ""

    for i in str(age):
        answer += l[int(i)]
    return answer

def other_sol(age):
    return "".join([chr(int(i) + 97) for i in str(age)])

print(solution(23))
print(solution(51))
print(solution(100))
print(other_sol(23))

# 'A' => 65
# 'a' => 97