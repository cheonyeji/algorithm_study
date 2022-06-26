# 2022-06-26
# 이코테 열흘동안 뽀개기 프로젝트 3일차
# dfs bfs 실전 4 미로 탈출
# 소요 시간 : 19:22 ~ 19: 41 (20m)

from collections import deque

n, m = map(int, input().split())

array = []

for _ in range(n):
    array.append(list(map(int, input())))

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr > n - 1 or nc < 0 or nc > m - 1:
                continue

            if array[nr][nc] == 1:
                array[nr][nc] = array[r][c] + 1
                q.append((nr, nc))

    return array[n - 1][m - 1]


print(bfs(0, 0))

"""
TC -> 10
5 6
101010
111111
000001
111111
111111
"""
