# 2023-04-18
# 백준 - DFS/BFS
# https://www.acmicpc.net/problem/7576
# 소요 시간 : 16:35 ~ 17:30 (55m)

from sys import stdin
from collections import deque

input = stdin.readline

M, N = map(int, input().split())  # M : col, N : row
graph = []

q = deque()

check_zero = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(M):
        if tmp[j] == 1:
            q.append((i, j))
        elif tmp[j] == 0:
            check_zero = 1
    graph.append(tmp)


def bfs():
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] > (graph[x][y] + 1) or graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))


# 토마토 익히기
bfs()

# 모든 토마토가 익은 뒤
def checkTomato():
    maxDate = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            else:
                maxDate = max(maxDate, graph[i][j])
    return maxDate - 1  # 며칠 뒤에 다 익는지라서 -1


# 처음부터 모두 익어있는 경우
if check_zero == 0:
    print(0)
else:
    print(checkTomato())
