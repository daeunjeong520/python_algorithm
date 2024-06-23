# 배열 회전시키기
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)

    return list(numbers)


def other_sol(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == "right" else numbers[1:] + [numbers[0]]

print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))
print(other_sol([1, 2, 3], "right"))
print(other_sol([4, 455, 6, 4, -1, 45, 6], "left"))
