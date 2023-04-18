# 2023-04-18
# 백준 2178 - DFS/BFS
# https://www.acmicpc.net/problem/2178
# 소요 시간 : 15:51 ~ 16:32 (40m)

"""
최단거리 문제 풀때 거리 체크하는 방법은 계속해서 바문하는 칸의 거리를 +1씩 해주면서 전진하면 ok
"""

from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int, input().split())  # N : row, M : col

graph = [list(input()) for _ in range(N)]  # graph에 현재 문자열로 들어가있고 줄바꿈
visit = [[False] * M for _ in range(N)]
q = deque()


def bfs(r, c):
    q.append((r, c))
    visit[r][c] = True

    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny] and graph[nx][ny] != "0":
                    visit[nx][ny] = True
                    graph[nx][ny] = int(graph[x][y]) + 1
                    q.append((nx, ny))


bfs(0, 0)
print(graph[N - 1][M - 1])
