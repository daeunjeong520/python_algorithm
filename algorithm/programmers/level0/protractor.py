# 각도기
def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    else:
        return 4

print(solution(70))
print(solution(91))
print(solution(180))