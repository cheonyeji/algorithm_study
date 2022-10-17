# 2022-10-17
# week3 - 재귀함수와 정렬.
# https://www.acmicpc.net/problem/
# 소요시간 : 16:42 ~ 16:43 (1m)

import sys

input = sys.stdin.readline

N = int(input())

data = [int(input()) for _ in range(N)]

data.sort()

for d in data:
    print(d)
