# 개미 군단
def solution(hp):
    attack = [5, 3, 1]
    ant_cnt = 0
    i = 0

    while hp >= 0:
        if(i == len(attack)):
            break
        ant_cnt += hp // attack[i]
        hp = hp % attack[i]
        i += 1

    return ant_cnt

def other_sol(hp):
    return hp // 5 + (hp % 5) // 3 + ((hp % 5) % 3)

print(solution(23))
print(solution(24))
print(solution(999))