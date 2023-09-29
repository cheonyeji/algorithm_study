# 2023-09-28 (소요시간 : 15m)
# 문제집 https://www.acmicpc.net/workbook/view/8708
# 골드5. https://www.acmicpc.net/problem/14719

from sys import stdin

input = stdin.readline

H, W = map(int, input().split(" "))  # row, col

graph = list(map(int, input().split(" ")))


rain = [0 for _ in range(W)]

for i in range(W):
    # 왼쪽 보기
    if i - 1 >= 0:
        for j in range(i - 1, -1, -1):
            # 빗물이 고일 수 있음
            if graph[j] >= graph[i]:
                for k in range(j, i + 1):
                    rain[k] = max(rain[k], graph[i] - graph[k])
                break

    # 오른쪽 보기
    if i + 1 < W:
        for j in range(i + 1, W):
            # 빗물 고이기 가능
            if graph[j] >= graph[i]:
                for k in range(i + 1, j + 1):
                    rain[k] = max(rain[k], graph[i] - graph[k])
                break


print(sum(rain))
