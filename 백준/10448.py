# 2023-04-24
# 백준 - 브루트 포스
# https://www.acmicpc.net/problem/10448
# 소요 시간 : 23:15 ~ 23:35 (20m)

from sys import stdin

input = stdin.readline

TC = int(input())
data = []
for _ in range(TC):
    data.append(int(input()))


allNums = [n * (n + 1) // 2 for n in range(1, 46)]
eureka_hit = [0] * 1001

for i in allNums:
    for j in allNums:
        for k in allNums:
            if i + j + k <= 1000:
                eureka_hit[i + j + k] = 1


for num in data:
    print(eureka_hit[num])
