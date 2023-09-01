# 2023-09-01 (소요시간 : 30m pypy로 통과)
# 그래프 [골드5. 백준 2589 보물섬] (https://www.acmicpc.net/problem/2589)

from sys import stdin
from collections import deque

input = stdin.readline

ROW, COL = map(int, input().split(" "))

graph = [list(input().rstrip()) for _ in range(ROW)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(sr, sc):
    visit = [[-1 for _ in range(COL)] for _ in range(ROW)]
    max_val = -int(1e9)
    q = deque([(sr, sc)])
    visit[sr][sc] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < ROW and 0 <= nc < COL:
                if graph[nr][nc] == "L" and visit[nr][nc] == -1:
                    visit[nr][nc] = visit[r][c] + 1
                    max_val = max(visit[nr][nc], max_val)
                    q.append((nr, nc))
    return max_val


answer = -int(1e9)
for r in range(ROW):
    for c in range(COL):
        if graph[r][c] == "L":
            # 위아래가 육지라면
            if 0 <= r - 1 < ROW and 0 <= r + 1 < ROW:
                if graph[r - 1][c] == "L" and graph[r + 1][c] == "L":
                    continue
            # 양옆이 육지라면
            if 0 <= c - 1 < COL and 0 <= c + 1 < COL:
                if graph[r][c - 1] == "L" and graph[r][c + 1] == "L":
                    continue
            answer = max(answer, bfs(r, c))

print(answer)
