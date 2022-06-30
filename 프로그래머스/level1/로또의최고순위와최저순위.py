# 2022-06-30
# 프로그래머스 lv1 - 로또의 최고 순위와 최저 순위
# https://programmers.co.kr/learn/courses/30/lessons/77484
# 소요 시간 : 23:05 ~ 23:10 (5m)


def setGrade(hit):
    if hit == 6:
        return 1
    elif hit == 5:
        return 2
    elif hit == 4:
        return 3
    elif hit == 3:
        return 4
    elif hit == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []

    # 0의 개수
    zero = lottos.count(0)

    # 일치 번호 수
    hit = 0

    for l in lottos:
        if l in win_nums:
            hit += 1

    if zero == 0:
        answer = [setGrade(hit), setGrade(hit)]
    else:
        answer = [setGrade(hit + zero), setGrade(hit)]

    return answer
