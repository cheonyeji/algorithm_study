# 2022-01-18
# 이코테 ch8 다이나믹 프로그래밍 실전 문제 4. 바닥 공사
# https://www.acmicpc.net/problem/11727

# 작은 것부터 차근차근!!!

n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] * 2

print(d[n] % 796796)
