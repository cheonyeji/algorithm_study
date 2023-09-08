# 2023-06-09
# 백준 - DP
# https://www.acmicpc.net/problem/2579
# 소요 시간 : 23:40 ~ 00:00 (20m)


"""
dp[0]에는 계단 0
dp[1]에는 계단 0, 1 (연속2계단) 
dp[2]에는 계단0, 2 (1계단건너뜀) vs 계단1,2 (연속2계단) 중 큰 값
dp[3]부터 연속2계단일때와 1계단 건너뛴 경우를 비교해서 최댓값을 넣어주기
"""
from sys import stdin

input = stdin.readline

N = int(input())
stair = [0] * 301

for i in range(N):
    stair[i] = int(input())

dp = [0] * 301
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, N):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

print(dp[N - 1])
