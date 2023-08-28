# 2023-08-28 (소요시간 : 16m)
# 누적합 https://www.acmicpc.net/problem/15724

from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))  # N : len(graph), M : len(graph[0])

graph = [list(map(int, input().split(" "))) for _ in range(N)]

acc = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

# 2차원 누적합 배열 구하기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        acc[i][j] = (
            acc[i - 1][j] + acc[i][j - 1] + graph[i - 1][j - 1] - acc[i - 1][j - 1]
        )

K = int(input())

# 구간 내 2차원 배열 누적합 구하기
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split(" "))
    print(acc[x2][y2] - acc[x1 - 1][y2] - acc[x2][y1 - 1] + acc[x1 - 1][y1 - 1])
