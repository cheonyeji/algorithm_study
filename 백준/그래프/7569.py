# 2023-09-04 (소요시간 : 1h)
# 그래프 [골드5. 백준 7569 토마토] (https://www.acmicpc.net/problem/7569)

from sys import stdin
from collections import deque

input = stdin.readline
# M : col, N : row, H : height
M, N, H = map(int, input().split(" "))

graph = []
tomato = deque([])
for h in range(H):
    temp = []
    for r in range(N):
        data = list(map(int, input().split(" ")))
        for c in range(M):
            if data[c] == 1:
                tomato.append((h, r, c))
        temp.append(data)
    graph.append(temp)

# 6가지 방향 고려
# 3차원 기준 상하, 2차원 기준 상하좌우
dir_ = [[1, 0, 0], [-1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1], [0, 0, -1]]


def bfs():
    while tomato:
        h, r, c = tomato.popleft()
        for i in range(len(dir_)):
            nh = h + dir_[i][0]
            nr = r + dir_[i][1]
            nc = c + dir_[i][2]

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                # 빈 칸
                if graph[nh][nr][nc] == -1:
                    continue
                # 안 익은 토마토
                if graph[nh][nr][nc] == 0:
                    graph[nh][nr][nc] = graph[h][r][c] + 1
                    tomato.append((nh, nr, nc))


# 모든 토마토가 익어있는 상태
if len(tomato) == H * M * N:
    print(0)

else:
    bfs()

    # 만약 0이 한개라도 존재한다면 -1 출력
    # 아니면 가장 큰 값-1 출력
    max_date = -int(1e9)
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if graph[h][r][c] == 0:
                    print(-1)
                    exit(0)
                max_date = max(max_date, graph[h][r][c])

    print(max_date - 1)
