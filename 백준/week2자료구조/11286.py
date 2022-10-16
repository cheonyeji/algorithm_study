# 2022-10-16
# week2 - 자료구조. 절댓값 힙
# https://www.acmicpc.net/problem/11286
# 소요시간 : 21:03 ~ 21:07 (5m)

"""
최소 힙인데 절댓값이 작은 것을 출력하되, 절댓값이 가장 작은 값이 여러 개면
가장 작은 수를 출력해야 함.
따라서 [abs(n), n] 를 넣어 먼저 절댓값 기준, 다음 원본 숫자 기준으로 최소 힙 만족하도록 값 넣
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())
commands = [int(input()) for _ in range(N)]

hq = []

for c in commands:
    if c == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, [abs(c), c])
