# 2022-10-16
# week2 - 자료구조. 최소 힙
# https://www.acmicpc.net/problem/1927
# 소요시간 : 20:56 ~ 21:01 (5m)

import heapq
import sys

input = sys.stdin.readline

N = int(input())
commands = [int(input()) for _ in range(N)]


min_heap = []
for c in commands:
    if c == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, c)
