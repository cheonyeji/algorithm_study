# 2023-09-01 (소요시간 : 2h)
# 구현 [골드3. 백준 16236 아기 상어] (https://www.acmicpc.net/problem/16236)


from sys import stdin
from collections import deque

input = stdin.readline
N = int(input())

# 물고기의 수
fish = 0

# 상어 좌표
sharkX, sharkY = 0, 0

# 상어 크기
shark_size = 2

# 상어가 먹은 물고기의 수
eat = 0

# 그래프 입력받기
graph = []
for i in range(N):
    data = list(map(int, input().split(" ")))
    for j in range(N):
        if data[j] != 0 and data[j] != 9:
            fish += 1
        elif data[j] == 9:
            sharkX, sharkY = i, j
    graph.append(data)

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(sr, sc, cnt, visit):
    q = deque([(sr, sc)])
    visit[sr][sc] = cnt
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] <= shark_size and visit[nr][nc] == 0:
                    visit[nr][nc] = visit[r][c] + 1
                    q.append((nr, nc))


def check(visit):
    fish_pos_dist = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] != 0 and 1 <= graph[i][j] < shark_size:
                fish_pos_dist.append((visit[i][j], i, j))
    return fish_pos_dist


graph[sharkX][sharkY] = 0
answer = 0
while fish > 0:
    visit = [[0 for _ in range(N)] for _ in range(N)]
    bfs(sharkX, sharkY, answer, visit)
    fish_pos_dist = check(visit)

    # 물고기의 수가 남아있어도 먹을 수 있는 물고기가 없을 수 있음
    if len(fish_pos_dist) == 0:
        break
    fish_pos_dist.sort(key=lambda x: (x[0], x[1], x[2]))

    dist, x, y = fish_pos_dist[0]
    # 물고기 먹기
    eat += 1
    fish -= 1
    graph[x][y] = 0
    if shark_size == eat:
        shark_size += 1
        eat = 0
    sharkX, sharkY = x, y
    answer = dist

print(answer)
