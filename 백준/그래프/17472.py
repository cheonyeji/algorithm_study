# 2023-09-06 (소요시간 : 1h 5m)
# 그래프 [골드1. 백준 17472 다리 만들기 2] (https://www.acmicpc.net/problem/17472)

from sys import stdin
from collections import deque

input = stdin.readline

# N : Row, M : Col
N, M = map(int, input().split(" "))

graph = [list(map(int, input().split(" "))) for _ in range(N)]
islands = []

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def find_island(sr, sc):
    temp = [(sr, sc)]
    q = deque([(sr, sc)])
    graph[sr][sc] = 2  # 방문처리
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1:
                    # 방문처리, 큐에 넣기, 섬 좌표값 저장
                    graph[nr][nc] = 2
                    q.append((nr, nc))
                    temp.append((nr, nc))

    islands.append(temp)


for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            find_island(r, c)


def find_island_idx(r, c):
    for i in range(len(islands)):
        if (r, c) in islands[i]:
            return i


dist = []
# idx : 섬 번호
for idx in range(len(islands)):
    for r, c in islands[idx]:
        # 섬 좌표 별로 4방향으로 쭉 직진하면서 다른 섬이 있는지 체크
        for i in range(4):
            count = 0
            nr = r + dr[i]
            nc = c + dc[i]
            while 0 <= nr < N and 0 <= nc < M:
                # 바다
                if graph[nr][nc] == 0:
                    nr += dr[i]
                    nc += dc[i]
                    count += 1
                # 섬
                else:
                    other_island = find_island_idx(nr, nc)
                    if idx != other_island and count != 1:
                        if (other_island, idx, count) not in dist:
                            dist.append((idx, other_island, count))
                    break

parent = [i for i in range(len(islands))]


def find_parent(parent, n):
    if parent[n] != n:
        parent[n] = find_parent(parent, parent[n])
    return parent[n]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


bridge = 0
answer = 0
dist.sort(key=lambda x: (x[2]))
for a, b, cost in dist:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        bridge += 1
        answer += cost

# 모든 섬이 연결되었는지 체크
if bridge != len(islands) - 1:
    print(-1)
else:
    print(answer)
