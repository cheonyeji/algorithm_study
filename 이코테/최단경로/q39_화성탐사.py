# 2022-01-11
# 이코테 ch17 최단 경로 문제 Q39 화성 탐사

# 다이나믹 프로그래밍으로 풀면 안됨...
# 테케 2번에서 20이 나오면 안되서 이렇게 접근x
def solution_dp():
    n = int(input())
    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                graph[i][j] = graph[i][j - 1] + graph[i][j]
            elif j == 0:
                graph[i][j] = graph[i - 1][j] + graph[i][j]
            else:
                graph[i][j] = min(
                    graph[i - 1][j] + graph[i][j], graph[i][j - 1] + graph[i][j]
                )

    return graph[n - 1][n - 1]


# 완전 이해를 잘못했어서 풀이 참고
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution_dijkstra():
    n = int(input())
    distance = [[INF] * n for _ in range(n)]

    graph = []

    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # 기존 다익스트라 알고리즘에 비해 노드 번호였던 것이 좌표로 수정된 것뿐
    x, y = 0, 0  # 시작위치 (0,0)
    # 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < o or ny >= n:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    return graph[n - 1][n - 1]


t = int(input())  # 테케 수
answer = []
for _ in range(t):
    answer.append(solution_dijkstra())

print(answer)

"""
테스크케이스
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
 """
