# 2021-02-01
# 이코테 ch13 DFS/BFS 문제 Q16 연구소
# https://www.acmicpc.net/problem/14502

import copy
from itertools import combinations


n, m = map(int, input().split())  # n:세로(행) m:가로(열)

graph = [list(map(int, input().split())) for _ in range(n)]

space = []
virus = []

for r in range(n):
    for c in range(m):
        # 빈칸 중 벽을 세울 수 있는 경우 3가지를 뽑아야하므로 좌표값 저장
        if graph[r][c] == 0:
            space.append([r, c])
        elif graph[r][c] == 2:
            virus.append([r, c])

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def go_virus(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            go_virus(graph, nx, ny)


safe_area = -1
# 빈칸 중 3칸의 벽을 세우는 경우를 모두 뽑아내기 (조합)
for cases in list(combinations(space, 3)):
    copied_graph = copy.deepcopy(graph)
    count = 0
    for case in cases:
        copied_graph[case[0]][case[1]] = 1

    # 전파 후 안전영역 계산
    for v in virus:
        go_virus(copied_graph, v[0], v[1])

    for r in range(n):
        for c in range(m):
            if copied_graph[r][c] == 0:
                count += 1

    safe_area = max(safe_area, count)

    # # 계산 후 다시 벽 허물기
    # for case in cases:
    #     graph[case[0]][case[1]] = 0

print(safe_area)

"""
TC -> 27
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""
