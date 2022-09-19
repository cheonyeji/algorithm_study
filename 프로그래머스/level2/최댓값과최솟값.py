# 2022-09-19
# 프로그래머스 lv2 - 최댓값과 최솟값
# https://school.programmers.co.kr/learn/courses/30/lessons/12939
# 소요 시간 : 11:29 ~ 11:39 (10m)


def solution(s):
    list_s = list(map(int, s.split(" ")))

    answer = str(min(list_s)) + " " + str(max(list_s))
    return answer
