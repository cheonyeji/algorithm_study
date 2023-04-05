# 2023-04-05
# 프로그래머스 고득점 kit - 완전탐색
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 소요 시간 : 13:53 ~ 14:14 (20m)


def solution(sizes):
    answer, maxW, maxH = 0, 0, 0
    for size in sizes:
        w, h = size
        # 최초의 경우
        if maxW == 0 and maxH == 0:
            maxW, maxH = w, h
        # 아닌 경우
        else:
            # 현재 max값과 비교해서 업데이트 발생 시 더 작은 넓이의 데이터 pick
            originalW, originalH = max(maxW, w), max(maxH, h)
            crossW, crossH = max(maxW, h), max(maxH, w)
            if (originalW * originalH) >= (crossW * crossH):
                maxW, maxH = crossW, crossH
            else:
                maxW, maxH = originalW, originalH

    answer = maxW * maxH

    return answer


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
