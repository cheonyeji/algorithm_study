# 2023-04-12
# 프로그래머스 고득점 kit - DFS/BFS
# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 소요 시간 : 17:26 ~ 18:10 (40m)

from collections import deque


def bfs(maps, r, c, visited):
    q = deque()
    q.append((r, c))
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    visited[r][c] = True

    while q:
        r, c = q.popleft()
        for i in range(len(dr)):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr <= len(maps) - 1 and nc <= len(maps[0]) - 1 and nr >= 0 and nc >= 0:
                if maps[nr][nc] == 1 and not visited[nr][nc]:
                    maps[nr][nc] = maps[r][c] + 1
                    visited[nr][nc] = True
                    q.append((nr, nc))


def solution(maps):
    answer = 0

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]  # 크기 주의
    bfs(maps, 0, 0, visited)

    if maps[len(maps) - 1][len(maps[0]) - 1] == 1:
        answer = -1
    else:
        answer = maps[len(maps) - 1][len(maps[0]) - 1]
    return answer


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
)
