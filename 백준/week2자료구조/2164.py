# 2022-10-16
# week2 - 자료구조. 카드2
# https://www.acmicpc.net/problem/2164
# 소요시간 : 11:44 ~ 12:04 (20m)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
dq = deque()

for i in range(1, N + 1):
    dq.append(i)

while len(dq) > 1:
    # 제일 위 카드 버림
    dq.popleft()
    dq.append(dq.popleft())


print(dq.pop())
