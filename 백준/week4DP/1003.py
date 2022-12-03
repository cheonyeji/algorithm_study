# 2022-12-03
# week4 - DP. 피보나치 함수
# https://www.acmicpc.net/problem/1003
# 소요 시간 : 17:46 ~ 18:16 (30m)

import sys

input = sys.stdin.readline

MAX = 40
dp_table = [[0, 0]] * (MAX + 1)  # 0, 1 등장 횟수

for i in range(len(dp_table)):
    if i == 0:
        dp_table[i] = [1, 0]
    elif i == 1:
        dp_table[i] = [0, 1]
    else:
        dp_table[i] = [
            dp_table[i - 1][0] + dp_table[i - 2][0],
            dp_table[i - 1][1] + dp_table[i - 2][1],
        ]


t = int(input())
for _ in range(t):
    n = int(input())
    print(" ".join(map(str, dp_table[n])))
