# 2023-09-01 (소요시간 : 30m)
# 그래프 [실버1. 백준 2583 영역 구하기] (https://www.acmicpc.net/problem/2583)

from sys import stdin
from collections import deque

input = stdin.readline

M, N, K = map(int, input().split(" "))  # M : row, N : col, 사각형 개수

graph = [[0 for _ in range(N)] for _ in range(M)]


for _ in range(K):
    lc, lr, rc, rr = map(int, input().split(" "))

    for r in range(lr, rr):
        for c in range(lc, rc):
            # 색칠
            graph[r][c] = 1

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(sr, sc):
    count = 1
    q = deque([(sr, sc)])
    # 방문처리
    graph[sr][sc] = 2
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N:
                # 색칠X 영역
                if graph[nr][nc] == 0:
                    # 방문처리
                    graph[nr][nc] = 2
                    count += 1
                    q.append((nr, nc))
    return count


answer = []
for r in range(M):
    for c in range(N):
        if graph[r][c] == 0:
            answer.append(bfs(r, c))

answer.sort()
print(len(answer))
print(" ".join(map(str, answer)))
