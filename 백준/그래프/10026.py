# 2023-09-04 (소요시간 : 20m)
# 그래프 [골드5. 백준 10026 적록색약] (https://www.acmicpc.net/problem/10026)

from sys import stdin
from collections import deque

input = stdin.readline
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def blue_bfs(sr, sc, visit):
    q = deque([(sr, sc)])
    visit[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == "B" and not visit[nr][nc]:
                    visit[nr][nc] = True
                    q.append((nr, nc))


def red_bfs(sr, sc, visit):
    q = deque([(sr, sc)])
    visit[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == "R" and not visit[nr][nc]:
                    visit[nr][nc] = True
                    q.append((nr, nc))


def green_bfs(sr, sc, visit):
    q = deque([(sr, sc)])
    visit[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == "G" and not visit[nr][nc]:
                    visit[nr][nc] = True
                    q.append((nr, nc))


def red_green_bfs(sr, sc, visit):
    q = deque([(sr, sc)])
    visit[sr][sc] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if (graph[nr][nc] == "R" or graph[nr][nc] == "G") and not visit[nr][nc]:
                    visit[nr][nc] = True
                    q.append((nr, nc))


# 적록색약 X
count = 0
visit = [[False for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            if graph[r][c] == "B":
                blue_bfs(r, c, visit)
            elif graph[r][c] == "R":
                red_bfs(r, c, visit)
            else:
                green_bfs(r, c, visit)
            count += 1

print(count, end=" ")

# 적록색약 O
count = 0
visit = [[False for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            if graph[r][c] == "B":
                blue_bfs(r, c, visit)
            else:
                red_green_bfs(r, c, visit)
            count += 1
print(count, end="")
