import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수, 출발도시(c)
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

# 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # x->y 비용이 z


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

# 도달 가능 도시 개수
count = 0
# 총 걸리는 시간 (가장 멀리 있는 노드와의 최단 거리)
max_dist = 0
# distance에서 INF이 아닌 도시(도달가능)만 카운트
for d in distance:
    if d != INF:
        count += 1
        max_dist = max(max_dist, d)

print(count - 1, max_dist)
