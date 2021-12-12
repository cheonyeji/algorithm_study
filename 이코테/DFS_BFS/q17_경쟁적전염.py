# 백준 18405 경쟁적 전염
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]

# pypy3로는 재귀제한 10**6하면 메모리제한난대서 10**5로 풀어봤더니 시간초과다
# 재귀로는 풀면 안될거같다 너무 깊게 들어가나봄 BFS로 걍 빠꾸없이 바꾸자 ㅠㅠ
# def goVirus(row, col, vNum, visited):
#     if row < 0 or row > n - 1 or col < 0 or col > n - 1:
#         return
#     if graph[row][col] != 0 and not visited[row][col]:
#         visited[row][col] = True
#         col - 1 > 0 and goVirus(row, col - 1, graph[row][col], visited)
#         col + 1 < n and goVirus(row, col + 1, graph[row][col], visited)
#         row - 1 > 0 and goVirus(row - 1, col, graph[row][col], visited)
#         row + 1 < n and goVirus(row + 1, col, graph[row][col], visited)
#         """
#         # 재귀 깊이를 조금이라도 ... 줄여보자....
#         for i in range(4):
#             goVirus(row + dx[i], col + dy[i], graph[row][col])
#         """
#         return
#     elif graph[row][col] == 0 and vNum != 0:
#         # 전파
#         graph[row][col] = vNum
#         visited[row][col] = True
#     elif visited[row][col] and vNum < graph[row][col] and vNum != 0:
#         # 전파
#         graph[row][col] = vNum
#     elif graph[row][col] == 0 and vNum == 0:
#         visited[row][col] = True
#         return


# for t in range(s):
#     visited = [[False] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             goVirus(i, j, 0, visited)

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((0, graph[i][j], i, j))  # 바이러스의 시간, 종류, row, col 좌표 삽입
virus.sort()

# BFS
# def goVirus(row, col, vNum, visited):
#     queue = deque([(row, col, vNum)])

#     while queue:
#         r, c, virus = queue.popleft()
#         if r < 0 or r > n - 1 or c < 0 or c > n - 1:
#             continue
#         # 전염시켜야 할 노드
#         if graph[r][c] != 0 and not visited[r][c] and virus > 0:
#             for i in range(4):
#                 queue.append((r + dx[i], c + dy[i], graph[r][c]))
#             visited[r][c] = True
#         else:
#             if (virus < graph[r][c] or graph[r][c] == 0) and virus != 0:
#                 graph[r][c] = virus
#             if not visited[r][c]:
#                 # 전염X 노드
#                 for i in range(4):
#                     queue.append((r + dx[i], c + dy[i], 0))
#             visited[r][c] = True


def goVirus(virus):
    global s, graph
    queue = deque(virus)
    while queue:
        time, vType, r, c = queue.popleft()
        if time == s:
            return
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if graph[nr][nc] == 0:
                    graph[nr][nc] = vType  # sort해줬기 때문에 추가로 바이러스 타입은 신경 쓸 필요없음
                    queue.append((time + 1, vType, nr, nc))


goVirus(virus)
print(graph)

if graph[x - 1][y - 1] != 0:
    print(graph[x - 1][y - 1])
else:
    print(0)
