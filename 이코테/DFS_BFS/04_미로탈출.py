# 이코테 DFS/BFS : 예제 4번. 미로 탈출
from collections import deque

n, m = map(int, input().split())

# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

graph = [list(map(int, input())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]  # (sx,sy) <-> (x,y) 거리 계산


def bfs(graph, x, y):

    queue = deque([(x, y)])
    distance[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if y - 1 >= 0 and graph[x][y - 1] == 1 and distance[x][y - 1] == -1:
            queue.append((x, y - 1))  # 상
            distance[x][y - 1] = distance[x][y] + 1
        if y + 1 < m and graph[x][y + 1] == 1 and distance[x][y + 1] == -1:
            queue.append((x, y + 1))  # 하
            distance[x][y + 1] = distance[x][y] + 1
        if x - 1 >= 0 and graph[x - 1][y] == 1 and distance[x - 1][y] == -1:
            queue.append((x - 1, y))  # 좌
            distance[x - 1][y] = distance[x][y] + 1
        if x + 1 < n and graph[x + 1][y] == 1 and distance[x + 1][y] == -1:
            queue.append((x + 1, y))  # 우
            distance[x + 1][y] = distance[x][y] + 1


bfs(graph, 0, 0)
# print(distance)
print(distance[n - 1][m - 1])


"""
테스크케이스 / 출력 : 10
5 6
101010
111111
000001
111111
111111
"""
