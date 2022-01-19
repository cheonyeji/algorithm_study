# 2022-01-18
# 이코테 ch8 다이나믹 프로그래밍 실전 문제 5 효율적인 화폐 구성

# 아예 점화식 자체를 접근을 못했고, 불필요하게 수들을 더하고 뺐다
# 앞에서부터 차근차근 봤어야 했는데 또 차근차근을 못했다.... 끙

# https://www.acmicpc.net/problem/2294

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(money[i], m + 1):
        if d[j - money[i]] != 10001:
            d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
