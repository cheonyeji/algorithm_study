# 2022-09-19
# 프로그래머스 lv1 - 제일 작은 수 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12935?language=python3
# 소요 시간 : 11:20 ~ 11:25 (5m)


def solution(arr):
    arr.remove(min(arr))

    if len(arr) == 0:
        arr.append(-1)

    return arr
