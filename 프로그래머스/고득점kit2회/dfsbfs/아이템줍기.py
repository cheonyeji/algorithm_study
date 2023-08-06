# 2023-08-05 (2h걸려서 풀음)
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[0] * 102 for _ in range(102)]

    # 사각형 기준 그래프 그리기
    def drawRect(LBx, LBy, RTx, RTy):
        for x in range(LBx, RTx * 2 + 1):
            graph[x][LBy] = 1
            graph[x][RTy] = 1

        for y in range(LBy, RTy * 2 + 1):
            graph[LBx][y] = 1
            graph[RTx][y] = 1

    # 내부 선 지우기
    def eraseInner(LBx, LBy, RTx, RTy):
        for x in range((LBx + 1), RTx * 2):
            for y in range((LBy + 1), RTy * 2):
                graph[x][y] = 0

    for LBx, LBy, RTx, RTy in rectangle:
        drawRect(LBx, LBy, RTx, RTy)

    for LBx, LBy, RTx, RTy in rectangle:
        eraseInner(LBx, LBy, RTx, RTy)

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 좌 우 상 하

    def bfs(startX, startY):
        q = deque([(startX, startY)])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + move[i][0]
                ny = y + move[i][1]

                if (1 <= nx <= 102 and 1 <= ny <= 102) and graph[nx][ny] == 1:
                    if nx == startX and ny == startY:
                        continue
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))

    bfs(characterX, characterY)

    answer = graph[itemX * 2][itemY * 2]
    return answer


print(
    solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)
)  # 17
print(
    solution([[1, 1, 8, 4], [2, 2, 4, 9], [3, 6, 9, 8], [6, 3, 7, 7]], 9, 7, 6, 1)
)  # 11
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))  # 9
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))  # 15
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))  # 10
