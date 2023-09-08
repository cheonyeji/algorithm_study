# 2023-05-28
# 백준 - 그리디
# https://www.acmicpc.net/problem/1946
# 소요 시간 : 16:00 ~ 16:25 (25m)

from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = []
    for _ in range(N):
        first, second = map(int, input().split())
        data.append([first, second])

    data.sort(key=lambda x: x[0])
    count = 0
    prevData = 0
    for i in range(len(data)):
        if i == 0:
            prevData = data[i][1]
            count += 1
        else:
            if data[i][1] < prevData:
                prevData = data[i][1]
                count += 1

    print(count)
