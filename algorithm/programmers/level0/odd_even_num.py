# 짝수 홀수 개수
def solution(num_list):
    odd_cnt = 0
    even_cnt = 0

    for i in num_list:
        if i % 2 == 1:
            odd_cnt += 1
        else:
            even_cnt += 1

    return [even_cnt, odd_cnt]

def other_sol(num_list):
    arr = [0, 0]

    for i in num_list:
        arr[i%2] += 1

    return arr

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))