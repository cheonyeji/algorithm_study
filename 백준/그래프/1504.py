# 2023-09-06 (소요시간 : 40m)
# 최단거리 [골드4. 백준 1504 특정한 최단 경로] (https://www.acmicpc.net/problem/1504)

from sys import stdin
import heapq

input = stdin.readline

N, E = map(int, input().split(" "))

# 노드
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split(" "))


def dijkstr(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))  # 비용, 노드

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            next_node, next_node_cost = i
            cost = dist + next_node_cost
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


# 1번 정점에서 시작하는 거리 그래프
distance1 = [int(1e9) for _ in range(N + 1)]
dijkstr(1, distance1)

# v1번 정점에서 시작하는 거리 그래프
distanceV1 = [int(1e9) for _ in range(N + 1)]
dijkstr(v1, distanceV1)

# v2번 정점에서 시작하는 거리 그래프
distanceV2 = [int(1e9) for _ in range(N + 1)]
dijkstr(v2, distanceV2)

answer = 0
# 1->v1->v2->N
if (
    distance1[v1] != int(1e9)
    and distanceV1[v2] != int(1e9)
    and distanceV2[N] != int(1e9)
):
    answer = distance1[v1] + distanceV1[v2] + distanceV2[N]

# 1->v2->v1->N
if (
    distance1[v2] != int(1e9)
    and distanceV2[v1] != int(1e9)
    and distanceV1[N] != int(1e9)
):
    answer = min(answer, distance1[v2] + distanceV2[v1] + distanceV1[N])

if answer == 0:
    print(-1)
else:
    print(answer)
