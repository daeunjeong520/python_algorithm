# 배열의 유사도
def solution(s1, s2):
    return len([i for i in s1 if i in s2])

def other_sol(s1, s2):
    return len(set(s1) & set(s2))

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m", "dot"]))
print(other_sol(["a", "b", "c"], ["com", "b", "d", "p", "c"]))
print(other_sol(["n", "omg"], ["m", "dot"]))