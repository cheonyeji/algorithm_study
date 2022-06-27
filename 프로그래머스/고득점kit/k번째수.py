# 2022-06-27
# 프로그래머스 고득점 kit - 정렬 k번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748
# 소요 시간 : 15:35 ~ 15:40 (5m)


def solution(array, commands):
    answer = []
    for c in commands:
        tmp = array[c[0] - 1 : c[1]]
        tmp.sort()
        answer.append(tmp[c[2] - 1])
    return answer
