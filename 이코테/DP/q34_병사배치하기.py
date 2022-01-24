# 2022-01-24
# 이코테 ch16 다이나믹 프로그래밍 Q34 병사 배치하기
# https://www.acmicpc.net/problem/18353

n = int(input())
data = list(map(int, input().split()))

# 가장 긴 감소하는 부분 수열
data.reverse()

dp = [1] * (n)

for i in range(1, n):
    for j in range(0, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

"""
TC -> 2
7
15 11 4 8 5 2 4
"""
