# 369게임
def solution(order):
    return len([i for i in str(order) if i in ["3", "6", "9"]])

def other_sol(order):
    return sum((map(lambda x: str(order).count(x), ["3", "6", "9"])))


print(solution(3))
print(solution(29423))
print(other_sol(3))
print(other_sol(29423))