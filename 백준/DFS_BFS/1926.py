# 2023-04-18
# 백준 1926 그림 - DFS/BFS
# https://www.acmicpc.net/problem/1926
# 소요 시간 : 14:34 ~ 15:11 (40m)

from sys import stdin
from collections import deque

input = stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]

visit = [[False] * col for _ in range(row)]
q = deque()


def bfs(r, c):
    count = 1
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]
    q.append((r, c))
    visit[r][c] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if graph[nx][ny] == 1 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    count += 1

    return count


pictures = []
for r in range(row):
    for c in range(col):
        if graph[r][c] == 1 and not visit[r][c]:
            pictures.append(bfs(r, c))


print(len(pictures))
if len(pictures) == 0:  # 그림이 하나도 없을때 예외처리
    print(0)
else:
    print(max(pictures))
