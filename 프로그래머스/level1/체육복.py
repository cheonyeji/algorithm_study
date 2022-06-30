# 2022-06-30
# 프로그래머스 lv1 - 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
# 소요 시간 : 17:02 ~ 17:19 (20m)


def solution(n, lost, reserve):
    answer = 0

    cloth = [1 for _ in range(n + 1)]
    cloth[0] = 0

    for i in lost:
        cloth[i] -= 1

    for j in reserve:
        cloth[j] += 1

    # 먼저 앞학생 체크하고 뒤학생 보기
    for s in range(1, len(cloth)):
        if cloth[s] == 0:
            if s != 1 and cloth[s - 1] == 2:
                cloth[s], cloth[s - 1] = 1, 1
            elif s != len(cloth) - 1 and cloth[s + 1] == 2:
                cloth[s], cloth[s + 1] = 1, 1

    answer = cloth.count(1) + cloth.count(2)

    return answer
