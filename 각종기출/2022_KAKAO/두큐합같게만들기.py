# 2022-09-20
# 2022 카카오 테크 인턴십 기출 - 두 큐 합 같게 만들기 (프로그래머스 lv2)
# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 소요 시간 : 14:02 ~ 14:54 (52m)

from collections import deque


def solution(queue1, queue2):
    answer = 0

    deque1 = deque(queue1)
    deque2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    len1 = len(queue1)
    len2 = len(queue2)

    goal = (sum1 + sum2) / 2

    while len1 != 0 and len2 != 0:
        if sum1 == goal and sum2 == goal:
            return answer

        if answer > 300000:
            break

        if sum1 > sum2:
            value = deque1.popleft()
            deque2.append(value)
            sum1 -= value
            sum2 += value
            len1 -= 1
            len2 += 1
        elif sum1 < sum2:
            value = deque2.popleft()
            deque1.append(value)
            sum1 += value
            sum2 -= value
            len1 += 1
            len2 -= 1
        else:
            if sum1 == goal and sum2 == goal:
                return answer

        answer += 1

    answer = -1

    return answer
