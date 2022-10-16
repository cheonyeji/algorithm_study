# 2022-10-16
# week2 - 자료구조. 프린터 큐
# https://www.acmicpc.net/problem/1966
# 소요시간 : 13:00 ~ 13:28 (30m)

"""
인덱스를 저장하고 있는 큐, 우선순위를 저장하고 있는 큐 2개를 사용
순위 큐에서 popleft()했을 때 max값보다 크거나 같으면 출력
-> 인덱스 큐에서 popleft()한 값을 order에 저장
아니면 맨 뒤로 보내기. 다시 append()
-> 인덱스 큐에서 popleft()한 값을 다시 append()

M번째 문서가 몇번째로 인쇄됬느지를 묻는 문제이므로 index+1 출력
(인쇄순서는 1부터 시작)
"""


import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split(" "))
    priority = list(map(int, input().split(" ")))
    q = deque()
    idx = deque()

    for i in range(len(priority)):
        q.append(priority[i])
        idx.append(i)

    order = []

    while len(q) > 0:
        max_pri = max(q)
        front_pri = q.popleft()
        front_idx = idx.popleft()

        if front_pri >= max_pri:
            order.append(front_idx)
        else:
            q.append(front_pri)
            idx.append(front_idx)

    print(order.index(M) + 1)
