# 2022-12-14
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 소요 시간 : 16:05 ~ 16:30, 17:10 ~ 17:30 (45m)

"""
2022.12.14에 푼 방법인데 이렇게 빡구현할 필요 없었음
w,h 중 더 긴 길이를 가로로 지정해준 뒤, 가로 길이 후보/세로 길이 후보에서 가장 큰 값만 뽑으면 되는 문제였다....
"""


def calcul(mw, w, mh, h):
    total = 0
    if mw - w < 0:
        total += mw - w
        if mh - h < 0:
            total += mh - h
    else:
        if mh - h < 0:
            total += mh - h
    return total


def solution(sizes):
    answer = 0

    max_w, max_h = 0, 0
    for size in sizes:
        w, h = size
        if (max_w - w) > 0 and (max_h - h) > 0:
            continue
        elif (max_w - h) > 0 and (max_h - w) > 0:
            continue
        else:
            noRotate = calcul(max_w, w, max_h, h)
            yesRotate = calcul(max_w, h, max_h, w)

            if noRotate != 0 and yesRotate != 0:
                if noRotate > yesRotate:
                    max_w = max(max_w, w)
                    max_h = max(max_h, h)
                else:
                    max_w = max(max_w, h)
                    max_h = max(max_h, w)
    answer = max_w * max_h
    return answer
