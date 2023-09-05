# 2023-09-05 (소요시간 : 1h 해설참고)
# 그래프 [골드3. 백준 2206 벽 부수고 이동하기] (https://www.acmicpc.net/problem/2206)

from sys import stdin
from collections import deque

input = stdin.readline

# N : row, M : col
N, M = map(int, input().split(" "))

graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

visit = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]


def bfs(sr, sc):
    # 벽 안 부순 상태 : 0
    q = deque([(sr, sc, 0)])
    visit[sr][sc][0] = 1
    while q:
        r, c, wall = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc][wall] == 0:
                    # 벽이 아니라면 이동
                    if graph[nr][nc] == 0:
                        q.append((nr, nc, wall))
                        visit[nr][nc][wall] = visit[r][c][wall] + 1
                # 벽 아직 안 부쉈고, 벽인 경우
                if wall == 0 and graph[nr][nc] == 1:
                    # 벽 부순 상태 : 1
                    q.append((nr, nc, 1))
                    # 이전경로 + 1 저장
                    visit[nr][nc][1] = visit[r][c][wall] + 1


bfs(0, 0)
max_dist = int(1e9)
if visit[N - 1][M - 1][1] != 0:
    max_dist = min(max_dist, visit[N - 1][M - 1][1])
if visit[N - 1][M - 1][0] != 0:
    max_dist = min(max_dist, visit[N - 1][M - 1][0])

if max_dist == int(1e9):
    print(-1)
else:
    print(max_dist)
