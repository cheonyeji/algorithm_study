# 2022-04-07
# 프로그래머스 고득점 kit 그리디 - 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()

    deque_ppl = deque(people)

    for i in range(len(people)):
        if len(deque_ppl) >= 2:
            left = deque_ppl.popleft()
            right = deque_ppl.pop()
            # 한 쌍으로 나갈 수 있음
            if left + right <= limit:
                answer += 1
            # right가 너무 무거워서 범위를 나감
            else:
                deque_ppl.appendleft(left)
                answer += 1
        else:
            # 홀수명이 남은 경우
            if len(deque_ppl) == 1:
                answer += 1
            break

    return answer
