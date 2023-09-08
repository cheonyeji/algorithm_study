# 2023-06-09
# 백준 - DP
# https://www.acmicpc.net/problem/2748
# 소요 시간 : 21:40 ~ 21:45 (5m)

from sys import stdin

input = stdin.readline

N = int(input())

dp = [0] * 100
dp[1] = 1
dp[2] = 1

for i in range(3, N + 2):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[N])
