# 2022-07-22
# 프로그래머스 Lv2 - 주식가격
# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 95m 고민 후 해설 참고

from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        cnt = 0
        for j in queue:
            cnt += 1
            if j < price:
                break
        answer.append(cnt)
    return answer
