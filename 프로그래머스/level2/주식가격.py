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


# 효율성은 떨어지지만 예전에 안 돌아가던 코드 돌아가게 수정
def solution(prices):
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i + 1, len(prices)):
            cnt += 1
            if prices[j] < prices[i]:
                break
        answer.append(cnt)
    return answer
