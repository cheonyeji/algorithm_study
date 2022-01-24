# 2021-01-24
# Q34에서 등장하는 원 개념 문제
# https://www.acmicpc.net/problem/11053

n = int(input())
data = list(map(int, input().split()))

# data[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
dp = [1] * (n)

for i in range(1, n):
    for j in range(0, i):
        # 만약 현재 값이 앞의 값들보다 크면
        if data[j] < data[i]:
            # 앞의 값+1, 본인 중 큰 값으로 저장
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
"""
TC
6
10 20 10 30 20 50
"""
