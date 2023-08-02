from collections import deque


def solution(maps):
    N = len(maps)  # 행 row
    M = len(maps[0])  # 열 col

    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]

    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                elif maps[nr][nc] > 1:
                    maps[nr][nc] = min(maps[nr][nc], maps[r][c] + 1)

    print(maps)
    if maps[N - 1][M - 1] == 1:
        return -1
    else:
        return maps[N - 1][M - 1]


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)  # 	11
