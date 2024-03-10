from collections import deque
from sys import stdin

input = stdin.readline

N, M = map(int, input().split(" "))

graph = []
ices = deque([])

for i in range(N):
    data = list(map(int, input().split(" ")))
    for j in range(len(data)):
        if data[j] != 0:
            ices.append((i, j))
    graph.append(data)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(sr, sc, visited, graph):
    global N, M
    q = deque([(sr, sc)])
    count = 1
    while q:
        r, c = q.popleft()
        visited[r][c] = True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] != 0 and visited[nr][nc] == False:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    count += 1
    return count


year = 0
while True:
    year += 1
    # 바닷물에 녹이기
    sea_q = deque([])
    for r, c in ices:
        sea = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 0:
                    sea += 1
        sea_q.append(sea)

    while sea_q:
        r, c = ices.popleft()
        sea = sea_q.popleft()
        graph[r][c] = max(0, graph[r][c] - sea)
        # 아직 얼음
        if graph[r][c] > 0:
            ices.append((r, c))

    # 만일 다 녹아버렸으면
    if len(ices) == 0:
        print(0)
        break

    visited = [[False for _ in range(M)] for _ in range(N)]
    # 빙산이 2조각으로 쪼개졌나 체크
    count = bfs(ices[0][0], ices[0][1], visited, graph)
    if count != len(ices):
        print(year)
        break
