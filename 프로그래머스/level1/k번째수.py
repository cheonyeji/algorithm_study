# 2022-06-30
# 프로그래머스 lv1 - k번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748
# 소요 시간 : 15:17 ~ 15:23 (5m)


def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command[0], command[1], command[2]
        result = array[i - 1 : j]
        result.sort()

        answer.append(result[k - 1])

    return answer
